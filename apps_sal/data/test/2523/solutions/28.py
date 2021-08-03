S = input()
l = len(S)
cnt = (l + 1) // 2
n = l - cnt
b = S[l // 2]
if l % 2 == 0:
    for i in range(n):
        if S[l // 2 - i - 1] != b or S[l // 2 + i] != b:
            break
        cnt += 1
else:
    for i in range(n):
        if S[l // 2 - i - 1] != b or S[l // 2 + i + 1] != b:
            break
        cnt += 1
print(cnt)
