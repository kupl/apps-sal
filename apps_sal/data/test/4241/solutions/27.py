# -*- coding utf-8 -*-

MOD = 10 ** 9 + 7

S = input()
T = input()

ans = len(T)
for i in range(len(S) - len(T) + 1):
    match = 0
    for j in range(len(T)):
        if T[j] == S[i + j]:
            match += 1
    ans = min(ans, len(T) - match)


print(ans)
