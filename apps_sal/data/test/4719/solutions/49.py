n = int(input())
s = list(input() for _ in range(n))

alphabet = [[0] * n for _ in range(26)]

for i in range(n):
    for x in s[i]:
        alphabet[ord(x) % 97][i] += 1

ans = ''
for i in range(26):
    m = min(alphabet[i])
    if m != 0:
        for _ in range(m):
            ans += chr(i + 97)

print(ans)
