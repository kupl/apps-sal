#import sys
#sys.stdin = open("python/in", "r")

s = input()
enc = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
d = dict()
for i in range(len(enc)):
    d[enc[i]] = i
ans = 0
for c in s:
    x = bin(d[c])
    x = x.rjust(8, '0')
    ans += x.count('0') - 1

M0D = 10**9 +7
print(pow(3, ans, M0D))

