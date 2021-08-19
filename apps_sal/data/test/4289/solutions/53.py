N = int(input())
(T, A) = list(map(int, input().split()))
H = list(map(int, input().split()))
tmp = 10000
ans = 0
for i in range(N):
    x = T - H[i] * 0.006
    if A > x:
        b = A - x
    else:
        b = x - A
    if b < tmp:
        tmp = b
        ans = i + 1
print(ans)
