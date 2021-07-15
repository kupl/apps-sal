n, m = list(map(int, input().split()))
d = []

count_of_good = 0
good_on_level = []

for i in range(m):
    a, b = list(map(int, input().split()))
    d.append((a, b))

for on_level in range(1, 101):
    good = True
    for el in d:
        etaj = el[1]
        kv = el[0]
        if not ((etaj - 1) * on_level < kv <= etaj * on_level):
            good = False
            break
    if good:
        count_of_good += 1
        good_on_level.append(on_level)

ans = []

for i in good_on_level:
    if n % i == 0:
        ans.append(n // i)
    else:
        ans.append(n // i + 1)

if len(ans) == 1:
    print(ans[0])
    return

for i in range(1, len(ans)):
    if ans[i - 1] != ans[i]:
        print('-1')
        return

print(ans[0])

