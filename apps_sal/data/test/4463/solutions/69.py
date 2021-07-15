s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)

l = [''.join(s),''.join(t)]

if l == sorted(l) and l[0]!=l[1]:
    print('Yes')
else:
    print('No')
