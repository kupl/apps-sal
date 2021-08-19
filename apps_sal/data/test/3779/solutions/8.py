def gcd(a, b):
    return a if 0 == b else gcd(b, a % b)


(n, k) = map(int, input().split(' '))
den = list(map(int, input().split(' ')))
g = 0
for i in den:
    g = gcd(g, i)
d = []
dic = {}
i = 0
while i < k:
    val = i * g % k
    if not val in dic:
        d.append(val)
        dic[val] = 1
        i = i + 1
    else:
        i = i + 1
        continue
print(len(d))
d.sort()
for val in d:
    print(val, end=' ')
