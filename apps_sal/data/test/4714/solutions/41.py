A, B = list(map(int, input().split()))
ans = 0
for x in range(A, B + 1):
    S = str(x)
    if S == S[::-1]:
        ans += 1
print(ans)
