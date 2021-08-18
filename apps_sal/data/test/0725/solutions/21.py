n, m = map(int, input().split())

ss = set()

for i in range(n):
    s = set(input().split())
    ss = ss.union(s)

if len(ss.intersection(set(['C', 'M', 'Y']))) > 0:
    print("
else:
    print("
