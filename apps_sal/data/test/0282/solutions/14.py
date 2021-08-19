(n, d) = list(map(int, input().split()))
s = input()
x1 = 0
k = 0
m = False
while x1 != n - 1:
    if x1 == -1 or s[n - 1] != '1' or x1 == s.rfind('1', x1, x1 + d + 1):
        m = True
        break
    o = s.rfind('1', x1, x1 + d + 1)
    x1 = o
    k += 1
if m:
    print('-1')
else:
    print(k)
