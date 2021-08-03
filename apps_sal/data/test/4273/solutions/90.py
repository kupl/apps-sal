import itertools
n = int(input())
num = [0] * 5
name = ['M', 'A', 'R', 'C', 'H']
for _ in range(n):
    s = str(input())
    for i in range(5):
        if s[0] == name[i]:
            num[i] += 1
            break
num = [k for k in num if k != 0]
c = num.count(0)
if 2 <= c:
    print(0)
else:
    d = 0
    for h, j, l in itertools.combinations(num, 3):
        d += (h * j * l)
    print(d)
