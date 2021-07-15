import sys
#from io import StringIO
#sys.stdin = StringIO(open(__file__.replace('.py', '.in')).read())

n, k = list(map(int, input().split()))
s = input()

d = list(sorted(set(s)))
ld = len(d)
h = {}
for i in range(len(d)):
    h[d[i]] = i

if k > n:
    print(s + d[0] * (k - n))
    return

p = list(s[0:k])
t = list(p)

for i in range(k-1, -1, -1):
    if s[i] >= t[i]:
        j = h[s[i]]
        if j < ld - 1:
            t[i] = d[j+1]
            for m in range(i+1, len(t)):
                t[m] = d[0]
            print(''.join(t))
            return

