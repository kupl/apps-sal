from collections import defaultdict
n = int(input())
arr = list(map(int, input().split()))
list1 = [False] * (10 ** 5 + 1)
d = defaultdict(int)
count = 0
for i in range(n):
    d[arr[i]] += 1
for i in range(n - 1):
    d[arr[i]] -= 1
    if d[arr[i]] == 0:
        del d[arr[i]]
    if list1[arr[i]] == False:
        count += len(list(d.items()))
        list1[arr[i]] = True
print(count)
