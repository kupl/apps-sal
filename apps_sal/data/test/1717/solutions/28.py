from collections import defaultdict
n = int(input())
s = 1
keys = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
powers = defaultdict(lambda: 0)

for i in range(2, n + 1):
    for key in keys:
        x = i
        cur = 0
        while x > 0 and x % key == 0:
            x //= key
            cur += 1
        powers[key] = max(powers[key], cur)

# print(dict(powers))
for key in keys:
    s *= (key ** powers[key])
s += 1
print(s)

# for i in range(2, n+1):
#     print(i, s % i)
