n = int(input())
arr = list(map(int, input().split()))
d = dict()
for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(max(d.values()))
