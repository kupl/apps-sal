# 29
S = str(input())

ans = 100000
i = 0
while i < len(S) - 2:
    x = int(str(S[i]) + str(S[i + 1]) + str(S[i + 2]))
    ans = min(ans, abs(753 - x))
    i += 1

print(ans)
