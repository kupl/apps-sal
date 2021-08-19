input()
q = [int(x) for x in input().split()]
q.sort()
s = delta = sum(q)
for item in q:
    s += delta
    delta -= item
print(s - q[-1])
