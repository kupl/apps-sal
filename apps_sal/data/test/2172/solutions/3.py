n, m = [int(i) for i in input().split()]
d = dict()
for i in range(m):
    s, s2 = input().split()
    d[s] = s2
for s in input().split():
    if(len(d[s])<len(s)):
        print(d[s],end=' ')
    else:
        print(s,end=' ')

