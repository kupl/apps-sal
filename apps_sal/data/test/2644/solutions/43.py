import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
ans = []
tag = 1
prev = 0

for i in range(N):
    if P[i] == tag:
        for j in range(i - 1, prev - 1, -1):
            P[j], P[j + 1] = P[j + 1], P[j]
            ans.append(j + 1)

        for j in range(prev, i):
            if P[j] != j + 1:
                print(-1)
                return

        tag = i + 1
        prev = i

if len(ans) != N - 1:
    print(-1)
    return

for ans_i in ans:
    print(ans_i)
