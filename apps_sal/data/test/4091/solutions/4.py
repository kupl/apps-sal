import heapq

n,k = map(int, input().split())
a = list(enumerate(map(int, input().split()), 1))
s = heapq.nlargest(k, a, key = lambda x: x[1])
su = sum([si[1] for si in s])
s = sorted([si[0] for si in s])
s[-1] = n
for i in range(len(s)-1, 0, -1):
    s[i] -= s[i-1]

print(su)
print(*s)
