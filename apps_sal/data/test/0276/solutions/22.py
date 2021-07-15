a = int(input())
c = set()
for i in range(a):
    b = input()
    c.add(b)
d = []
if 'purple' not in c:
    d.append('Power')
if 'green' not in c:
    d.append('Time')
if 'blue' not in c:
    d.append('Space')
if 'orange' not in c:
    d.append('Soul')
if 'red' not in c:
    d.append('Reality')
if 'yellow' not in c:
    d.append('Mind')
print(len(d))
for i in d:
    print(i)

