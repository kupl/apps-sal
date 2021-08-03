s = input()
n = int(input())

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

dcl = list(d.values())

found = False
for x in range(1, 1001):
    if sum([(dc - 1) // x + 1 for dc in dcl]) <= n:
        found = True
        print(x)
        s = ''.join([key * ((d[key] - 1) // x + 1) for key in sorted(d.keys())])
        s += (n - len(s)) * 'a'
        print(s)
        break
if not found:
    print(-1)
