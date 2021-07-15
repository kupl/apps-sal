d = {}

s = input().split()
n = int(s[0])
m = int(s[1])

s = input().split()

for item in s:
    if item not in d.keys():
        d.update(dict([(item, 1)]))
    else:
        d[item] += 1

cur = 0

while True:
    num = 0
    for item in d.values():
        num += item // (cur + 1)
    if num < n:
        break
    cur += 1

print(cur)
