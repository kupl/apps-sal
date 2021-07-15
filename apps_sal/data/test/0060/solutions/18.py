s = input()
n = int(s[:-1])
s = s[-1:]
n -= 1
x = n // 4
ans = x * 16
n -= x * 4
d = dict()
d = {'f':1, 'e':2, 'd':3, 'a':4, 'b':5, 'c':6}
if n == 0 or n == 2:
    ans += d[s]
else:
    ans += (7 + d[s])
print(ans)

