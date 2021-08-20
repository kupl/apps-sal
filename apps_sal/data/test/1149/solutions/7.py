n = int(input())
a = list(map(int, input().split()))
p = a[0]
ps = a[1:]
a = list(map(int, input().split()))
q = a[0]
qs = a[1:]
s = set(ps) | set(qs)
if len(s) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
