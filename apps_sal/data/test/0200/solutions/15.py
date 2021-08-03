H1, H2 = list(map(int, input().split()))
A, B = list(map(int, input().split()))

num = H2 - H1 - 8 * A
den = 12 * (A - B)
if den > 0:
    ans = max(0, (num + den - 1) // den)
else:
    ans = 0 if num <= 0 else -1
print(ans)
