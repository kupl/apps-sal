import sys
input = sys.stdin.readline

t = int(input())

for test in range(t):

    S = input().strip() + "0"

    NOW = S[0]
    count = 1
    ANS = []

    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            count += 1
        else:
            if count % 2 == 1:
                ANS.append(S[i - 1])

            count = 1

    ANS = sorted(set(ANS))

    print("".join(ANS))
