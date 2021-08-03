s = input()
n, k, p = s.split(' ')
n = int(n)
k = int(k)
p = int(p)


def time(start):
    nonlocal people, keys, n, p
    res = 0
    for i in range(n):
        res = max(res, abs(people[i] - keys[i + start]) + abs(keys[i + start] - p))
    return res


s = input()
people = s.split(' ')
for i in range(n):
    people[i] = int(people[i])
s = input()
keys = s.split(' ')
for i in range(k):
    keys[i] = int(keys[i])
people.sort()
keys.sort()
res = 10**10
for i in range(k - n + 1):
    res = min(res, time(i))
print(res)
