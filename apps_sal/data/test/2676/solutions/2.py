t = int(input())
d = []
count = 0
for i in range(0, t):
    f = input()
    d.append(f)
d = list(set(d))
y = int(input())
r = input()
for l in range(0, len(d)):
    if d[l] in r:
        count += 1
print(count)
