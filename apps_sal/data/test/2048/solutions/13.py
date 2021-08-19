"""
R=lambda:[int(i)for i in input().split()]
I=3*10**8
n=int(input())
s,c=R(),R()
r=min(c[j]+min([I]+[c[i]for i in range(j)if
s[i]<s[j]])+min([I]+[c[i] for i in range(j+1,n)if
s[i]>s[j]])for j in range(n))
print((r,-1)[r>I])
"""


def R():
    return [int(i) for i in input().split()]


I = 3 * 10 ** 9
n = int(input())
(s, c) = (R(), R())
r = I
for j in range(n):
    t1 = I
    for i in range(j):
        if s[i] < s[j]:
            t1 = min(t1, c[i])
    t2 = I
    for i in range(j + 1, n):
        if s[i] > s[j]:
            t2 = min(t2, c[i])
    r = min(c[j] + t1 + t2, r)
if r < I:
    print(r)
else:
    print('-1')
