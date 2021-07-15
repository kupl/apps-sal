n,q = map(int,input().split())
s = input()
s = s.replace('AC','ac')
t = [0] * n
r = 0
for i in range(n):
    if s[i] == 'c':
        r += 1
    t[i] = r
for i in range(q):
    l,r = map(int,input().split())
    print(t[r-1]-t[l-1])
