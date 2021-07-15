n = int(input())
arr = [int(x) for x in input().split()]
new = [0]
for i in arr:
    new.append(i + new[-1])
k = min(new)
if max(new) - min(new) + 1 != n or len(set(new)) != n:
    print(-1)
else:
    for i in new:
        print(i - k + 1, end=' ')
