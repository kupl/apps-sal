import itertools

N = int(input())
t = tuple('MARCH')
dic = {}

for _ in range(N):
    s = input()
    x = s[0]

    if x not in t:
        continue

    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

count = [v for v in list(dic.values())]
if len(count) < 3:
    print((0))
    return

ans = 0
for a, b, c in itertools.combinations(count, 3):
    ans += a * b * c

print(ans)

