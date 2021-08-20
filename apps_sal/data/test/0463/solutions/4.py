(n, x) = list(map(int, input().split()))
a = sorted(map(int, input().split()))
s = set(a)
b = sorted([u & x for u in a])
t = set(b)
if len(s) < len(a):
    print(0)
elif any([u != u & x and u & x in s for u in a]):
    print(1)
elif len(t) < len(b):
    print(2)
else:
    print(-1)
