import sys

sys.setrecursionlimit(10 ** 7)

# ----------

INF = float("inf")
MOD = 10 ** 9 + 7

N, A, B, C = list(map(int, input().split()))
num = [A, B, C]
S = []
for i in range(N):
    S.append(input().strip())
S.append('AB')

ans = []
for i in range(N):
    s = S[i]
    s1 = s[0]
    s2 = s[1]
    n1 = num["ABC".index(s1)]
    n2 = num["ABC".index(s2)]
    if n1 == n2 == 0:
        print("No")
        return
    if n1 == 0:
        num["ABC".index(s1)] += 1
        num["ABC".index(s2)] -= 1
        ans.append(s1)
        continue
    if n2 == 0:
        num["ABC".index(s1)] -= 1
        num["ABC".index(s2)] += 1
        ans.append(s2)
        continue
    if s1 in S[i + 1]:
        num["ABC".index(s1)] += 1
        num["ABC".index(s2)] -= 1
        ans.append(s1)
    else:
        num["ABC".index(s1)] -= 1
        num["ABC".index(s2)] += 1
        ans.append(s2)

print('Yes')
for a in ans:
    print(a)

