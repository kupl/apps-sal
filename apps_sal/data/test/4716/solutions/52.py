
N, K = list(map(int, input().split()))
j = list(map(int, input().split()))
ans = 0

j.sort()
for i in range(K):
    ans += j.pop()

print(ans)
