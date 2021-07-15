A, B = list(map(int, input().split()))
ans = 0
for _ in range(2):
    ans += max(A, B)
    if A >= B:
        A -= 1
    else:
        B -=1
print(ans)

