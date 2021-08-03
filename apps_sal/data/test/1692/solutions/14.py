ch = input()
S = 0
for i in range(len(ch) - 1, -1, -1):
    if int(ch[i]) % 4 == 0:
        S = S + 1
    ch1 = ch[i - 1] + ch[i]
    if int(ch1) % 4 == 0:
        S = S + i
print(S)
