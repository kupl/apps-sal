(n, k) = (int(x) for x in input().split())
msg = [int(x) for x in input().split()]
stk = []
for m in msg:
    if m in stk:
        continue
    stk.insert(0, m)
    while len(stk) > k:
        stk.pop()
print(len(stk))
for i in stk:
    print(i, end=' ')
print()
