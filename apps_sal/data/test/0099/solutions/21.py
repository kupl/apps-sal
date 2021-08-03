B, Q, L, M = list(map(int, input().split()))
A = set(map(int, input().split()))
ans = 0
for _ in range(100):
    if abs(B) > L:
        break
    if B not in A:
        ans += 1
    B *= Q
print(ans if ans < 32 else "inf")
