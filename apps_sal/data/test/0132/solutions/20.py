import sys
data = sys.stdin.readlines()

n = int(data[0])
m = [int(x) for x in data[1].split()]

res = []

for k in range(n):
    for i in range(n):
        a = abs(sum(m[:i]) - sum(m[i:]))
        res.append(a)
    m.append(m[0])
    m = m[1:]
print(min(res))
        

