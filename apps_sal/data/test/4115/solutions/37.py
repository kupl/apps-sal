S = input()
if len(S) % 2 == 0:
    S_left = list(S)[:int(len(S) / 2)]
    S_right = list(S)[int(len(S) / 2):][::-1]

else:
    S_left = list(S)[:int(len(S) // 2)]
    S_right = list(S)[int(len(S) / 2) + 1:][::-1]

ans = 0
for i in range(len(S_left)):
    if S_left[i] != S_right[i]:
        ans += 1

print(ans)
