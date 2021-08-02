N, X = list(map(int, input().split()))
L = list(map(int, input().split()))

num = 1
s = 0
for i in range(N):
    s += L[i]
    if s > X: break
    num += 1

print(num)
