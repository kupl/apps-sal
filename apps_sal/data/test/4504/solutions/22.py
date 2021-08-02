S = input()
for i in range(1, len(S)):
    S_short = S[0:-i]
    if len(S_short) % 2 != 0:
        continue
    else:
        half = len(S_short) // 2
        if S_short[0:half] == S_short[half:]:
            break
        else:
            continue
print(len(S) - i)
