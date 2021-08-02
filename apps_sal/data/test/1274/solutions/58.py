import heapq
n, m = map(int, input().split())
limit = [[] for i in range(m)]
for i in range(n):
    a, b = map(int, input().split())
    if a > m:
        # 間に合わないので使えない
        continue
    # m-a日目までに取り掛かれば間に合うバイトを格納
    limit[m - a].append(b)

available = []
ans = 0
for i in range(m - 1, -1, -1):
    # 最終日から辿ることで、新たに選択不可となるバイトが生じない
    for item in limit[i]:
        heapq.heappush(available, -item)
    if available:
        ans += -heapq.heappop(available)
print(ans)
