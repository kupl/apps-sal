N = int(input())
(T, A) = list(map(int, input().split()))
H = list(map(int, input().split()))
ans = 1000000000000
for i in range(N):
    temp = T - H[i] * 0.006
    if abs(temp - A) < ans:
        ans = abs(temp - A)
        p = i + 1
print(p)
