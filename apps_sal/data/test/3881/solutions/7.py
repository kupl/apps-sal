n, q = map(int, input().split())
d = {}
ch = set()
ans = set()
for i in range(q):
    a, b = input().split()
    d.setdefault(b, set()).add(a)
ch = {"a"}

while ch != set():
    b = ch.pop()
    if len(b) == n:
        ans.add(b)
        continue
    for a in d.setdefault(b[0], set()):
        ch.add(''.join((a, b[1:])))
print(len(ans))
