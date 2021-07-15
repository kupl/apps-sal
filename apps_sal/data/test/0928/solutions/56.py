N, K = map(int, input().split())
A = list(map(int, input().split()))

s = [0]
for i in range(N):
    s.append(s[-1]+A[i])

l = 0
r = 1
cnt = 0

for l in range(N):
    while r < N and s[r] - s[l] < K:
        r += 1
    if s[r] - s[l] < K:
        break
    
    cnt += N - r + 1

    if l + 1 == r:
        r += 1

print(cnt)
