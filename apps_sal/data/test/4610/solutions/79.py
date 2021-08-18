import collections
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

a = collections.Counter(a)
key = list(a.values())
key.sort()
ans = sum(key[:len(key) - k])
print(ans)
