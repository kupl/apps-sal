S = input()
l = len(S)
ans = 0
for i in range(l):
    for j in range(i + 1, l + 1):
        temp = int(S[i:j])
        ans += temp * max(1, pow(2, i - 1)) * max(1, pow(2, l - j - 1))
print(ans)
