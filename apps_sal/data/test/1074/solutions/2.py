n = int(input())
n = str(bin(n))
n = n[2:]
while len(n) % 3 != 0:
    n = '0' + n
ans = 0
for i in range(0, len(n) // 3 + 1):
    if n[3 * i:3 * i + 3] == '001':
        ans += 1
print(ans)
