

from collections import defaultdict
n, k = list(map(int, input().split()))

la = list(map(int, input().split()))

mini = 10**18


hash = defaultdict(int)

for i in range(len(la)):
    z1 = i + 1
    z2 = n - i
    z = min(z1, z2)
    if la[i] in hash:
        hash[la[i]] = min(z, hash[la[i]])
    else:
        hash[la[i]] = z

for i in range(len(la)):
    z = k - la[i]
    if z in hash and z != la[i]:
        ans = max(hash[z], hash[la[i]])
        mini = min(mini, ans)


if mini == 10**18:
    print(-1)
else:
    print(mini)
