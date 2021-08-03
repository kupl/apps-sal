import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())
    S = input().strip()

    OPENING = -1
    for i in range(n):
        if S[i] == "1":
            OPENING = i
            break

    ENDING = n
    for i in range(n - 1, -1, -1):
        if S[i] == "0":
            ENDING = i
            break

    if OPENING == -1 or ENDING == n:
        print(S)
    elif OPENING > ENDING:
        print(S)
    else:
        print("".join(map(str, [0] * (OPENING + 1) + [1] * (n - 1 - ENDING))))
