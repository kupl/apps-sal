(n, k) = [int(c) for c in input().split(' ')]
aCode = ord('a')
(passwd, temp) = ('', '')
for i in range(0, k):
    temp += chr(aCode + i)
count = n // k
rest = n % k
passwd = temp * count
if rest > 0:
    passwd += temp[:rest]
print(passwd)
