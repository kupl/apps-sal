def mp():
    return map(int, input().split())

def f(n):
    nonlocal l
    res = []
    l = 0
    while n > 0:
        res.append(n % 2)
        n //= 2
        l += 1
    return res[::-1]

n = int(input())
l = 0
s = f(n)

cnt = 0
ans = []
h = len(s)
while n != 2 ** l - 1:
    if s[-1] == 0:
        ans.append(0)
        n += 1
        s = f(n)
        continue
    idx = (''.join(map(str, s))).find('0')
    #print(idx, h - idx)
    ans.append(h - idx)
    n ^= 2 ** (l - idx) - 1
    #print(n, n + 1)
    n += 1
    s = f(n)
    
print(len(ans) * 2)
for i in ans:
    print(i, end = ' ')
