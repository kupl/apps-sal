n = int(input())
L = [50] * 26
for i in range(n):
    S = input()
    for i in range(26):
        L[i] = min(L[i], S.count(chr(97 + i)))
ans = ''
for i in range(26):
    ans += chr(97 + i) * L[i]
print(ans)
