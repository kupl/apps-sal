n = int(input())
a = list(map(int, input().split()))
dict1 = {}
for i in range(1, n + 1):
    dict1[i] = []
for count, i in enumerate(a):
    dict1[i].append(count)
ans = 0
d = 0
s = 0
for i in range(1, n + 1):
    ans += abs(d - max(dict1[i]))
    ans += abs(s - min(dict1[i]))
    d = max(dict1[i])
    s = min(dict1[i])
print(ans)
