from collections import Counter
n = int(input())
a = input().split()
a = [int(i) for i in a]
ans = 0
'\nfor i in range(n):\n    ans += d.get(a[i],0)\n    for j in range(1,31):\n        val = 2**j - a[i]\n        if val > 0:\n            if val not in d:\n                d[val] = 1\n            else:\n                d[val] += 1\nprint(ans)\n'
d = Counter()
for i in range(n):
    for j in range(1, 31):
        val = 2 ** j - a[i]
        if val > 0:
            if val in d:
                ans += d[val]
    d[a[i]] += 1
print(ans)
