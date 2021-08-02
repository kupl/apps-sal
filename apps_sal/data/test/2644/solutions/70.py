import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
tage = 1
s = 0
ans = []

for i in range(N):
    if P[i] == tage:
        for j in range(i - 1, s - 1, -1):
            P[j], P[j + 1] = P[j + 1], P[j]
            ans.append(j)

        for j in range(s, i):
            if P[j] != j + 1:
                print(-1)
                return

        tage = i + 1
        s = i

if len(ans) != N - 1:
    print(-1)
    return

for ans_i in ans:
    print(ans_i + 1)
