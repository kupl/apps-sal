n = int(input())
w = list(map(int, input().split()))
ans = 10000
for i in range(n):
    w1 = sum(w[:i])
    w2 = sum(w[i:])
    if ans > abs(w1 - w2):
        ans = abs(w1 - w2)
print(ans)
