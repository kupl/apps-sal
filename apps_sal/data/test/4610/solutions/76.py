import collections
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
count = 0
b = len(collections.Counter(a))
c = collections.Counter(a).most_common()
# print(b)
for i in range(min(k, b)):
    count += c[i][1]
#    print(count)
ans = len(a) - count
print(ans)
