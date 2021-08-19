(N, X) = map(int, input().split())
L = list(map(int, input().split()))
s = 0
cnt = 1
for i in range(N):
    if s + L[i] > X:
        break
    s += L[i]
    cnt += 1
print(cnt)
