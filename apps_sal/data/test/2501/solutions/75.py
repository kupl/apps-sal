N = int(input())
L = [0] * (404040)
A = list(map(int, input().split()))
ans = 0
for i, a in enumerate(A):
    ia = i - a
    if ia >= 0:
        ans += L[ia]
    ai = a + i
    if ai < 404040:
        L[ai] += 1
print(ans)

