def solve(n, c, a1, a2):
    curr = 0
    ans = 0
    for i in range(n):
        curr += a2[i]
        ans += max(0, a1[i] - c * curr)
    return ans


n, c = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
s1 = s2 = 0
r1 = solve(n, c, a1, a2)
r2 = solve(n, c, a1[::-1], a2[::-1])
if r1 > r2:
    print("Limak")
elif r1 == r2:
    print("Tie")
else:
    print("Radewoosh")
