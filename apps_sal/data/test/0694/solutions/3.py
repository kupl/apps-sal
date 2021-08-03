# import sys
# sys.stdin = open("F:\\Scripts\\input","r")
# sys.stdout = open("F:\\Scripts\\output","w")


MOD = 10**9 + 7
def I(): return list(map(int, input().split()))


s = input()
a, b = I()
n = len(s)
x = [0] * n
y = [0] * n
x[0] = int(s[0]) % a
y[n - 1] = int(s[n - 1]) % b
p = 10 % b
for i in range(1, n):
    x[i] = (x[i - 1] * 10 + int(s[i])) % a
    y[n - i - 1] = (int(s[n - i - 1]) * p + y[n - i]) % b
    p *= 10
    p %= b
for i in range(n - 1):
    if not x[i] and not y[i + 1] and (s[i + 1] != '0'):
        print("YES", s[:i + 1], s[i + 1:], sep='\n')
        break
else:
    print("NO")
