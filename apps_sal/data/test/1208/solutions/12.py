n = int(input())
s = set()
now = set()
m = 0
for i in range(n):
    a = input().split()
    if a[0] == '+':
        now.add(a[1])
        s.add(a[1])
        if len(now) > m:
            m = len(now)
    elif a[1] not in s:
        m = max(m, len(now)) + 1
        s.add(a[1])
    else:
        now.discard(a[1])
print(m)
