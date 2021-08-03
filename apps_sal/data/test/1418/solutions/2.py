import sys
input = sys.stdin.readline

n = int(input())

ANS = [0] * (n + 1)

now = 1

for i in range(2, n + 1):
    if ANS[i] != 0:
        continue
    else:
        for j in range(i, n + 1, i):
            if ANS[j] == 0:
                ANS[j] = now

        now += 1

print(*ANS[2:])
