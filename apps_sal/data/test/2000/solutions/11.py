from collections import Counter

n = int(input())
a = input().split()
a = [int(i) for i in a]
ans = 0
'''
for i in range(n):
    ans += d.get(a[i],0)
    for j in range(1,31):
        val = 2**j - a[i]
        if val > 0:
            if val not in d:
                d[val] = 1
            else:
                d[val] += 1
print(ans)
'''
d = Counter()
for i in range(n):
    for j in range(1, 31):
        val = 2**j - a[i]
        if val > 0:
            if val in d:
                ans += d[val]
    d[a[i]] += 1
print(ans)
