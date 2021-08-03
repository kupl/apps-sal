import itertools
N = int(input())
A = [input() for i in range(N)]
dic = {}
ans = 0
for j in range(N):
    a = str(sorted(A[j]))
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1
        ans += dic[a] - 1

print(ans)
