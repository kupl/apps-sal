from collections import defaultdict
dic = defaultdict(int)
details = list(map(int, input().split()))
N = details[0]
M = details[1]
cards = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(M)]
for i in range(N):
    dic[cards[i]] += 1
for i in range(M):
    dic[ab[i][1]] += ab[i][0]
lst = sorted(dic.keys())
ans = 0
while N:
    if dic[lst[-1]] > 0:
        dic[lst[-1]] -= 1
        ans += lst[-1]
        N -= 1
    else:
        lst.pop()
print(ans)
