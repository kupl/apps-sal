import collections
n = int(input())
lis = [0] * n
for i in range(n):
    lis[i] = int(input())


ans = 0
lis = collections.Counter(lis)

for i in lis.values():
    if i % 2 == 1:
        ans += 1

print(ans)
