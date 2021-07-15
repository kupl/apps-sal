n = int(input())
alst = list(map(int, input().split()))
divisor_lst = [[0] for _ in range(n)]
ans = []
for i in range(2, n + 1):
    for k in range(i * 2, n + 1, i):
        divisor_lst[k - 1].append(i - 1)
for i in range(n - 1, -1, -1):
    if alst[i] == 1:
        for j in divisor_lst[i]:
            alst[j] += 1
            alst[j] %= 2
        ans.append(i + 1)
print(len(ans))
print(*ans)
