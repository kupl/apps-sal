def read():
    return [int(s) for s in input().split()]


s = input().strip()
res = 0
for i in range(len(s)):
    if int(s[i]) % 4 == 0:
        res += 1
for i in range(len(s) - 1):
    if int(s[i:i + 2]) % 4 == 0:
        res += i + 1
print(res)
