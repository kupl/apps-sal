S = input()
length = len(S)
if length % 2 == 0:
    length = int(length / 2)
    S_half_1 = S[:length]
    S_half_2 = S[(length):]
    S_half_2 = S_half_2[::-1]
else:
    length = int(length // 2)
    S_half_1 = S[:length]
    S_half_2 = S[(length + 1):]
    S_half_2 = S_half_2[::-1]

ans = 0
for i in range(length):
    if S_half_1[i] != S_half_2[i]:
        ans += 1
print(ans)
