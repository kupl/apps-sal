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
    s1 = S[i][0]
    s2 = S[i][1]
    n1 = num["ABC".index(s1)]
    n2 = num["ABC".index(s2)]

    if n1 == n2 == 0:
        print("No")
        return

    s_add = ""
    s_sub = ""
    if n1 == 0:
        s_add = s1
        s_sub = s2
    elif n2 == 0:
        s_add = s2
        s_sub = s1
    elif s1 in S[i + 1]:
        s_add = s1
        s_sub = s2
    else:
        s_add = s2
        s_sub = s1

    num["ABC".index(s_add)] += 1
    num["ABC".index(s_sub)] -= 1
    ans.append(s_add)

print('Yes')
for a in ans:
    print(a)

