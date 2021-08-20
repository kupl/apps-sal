data = input().rstrip().split()
n = int(data[0])
s = int(data[1])
su = 0
ma = 0
data = input().rstrip().split()
for i in range(n):
    a = int(data[i])
    su += a
    if ma < a:
        ma = a
su -= ma
print('YES' if su <= s else 'NO')
