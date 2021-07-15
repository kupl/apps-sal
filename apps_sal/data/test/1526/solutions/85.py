A, B, C = map(int, input().split())
ans = max(A, B, C)*3 - (A + B + C)
if ans % 2 == 1:
    ans += 3
print(ans // 2)
