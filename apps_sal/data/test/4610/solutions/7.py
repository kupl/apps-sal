import collections

n, k = map(int,input().split())
a = list(map(int, input().split()))

c = collections.Counter(a)
i = 0
cnt = 0
for key, val in sorted(c.items(), key=lambda x: -x[1]):
    # print(key, val)
    cnt += val
    i += 1
    if i >= k:
        break
        
print(n - cnt)
