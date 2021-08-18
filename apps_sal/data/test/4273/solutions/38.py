from itertools import combinations as com
n = int(input())
D = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
for i in range(n):
    s = input()
    if s[0] in ["M", "A", "R", "C", "H"]:
        D[s[0]] += 1

ans = 0
A = list(D.values())
for l in com(list(range(5)), 3):
    ans += A[l[0]] * A[l[1]] * A[l[2]]
print(ans)
