"""n = int(input())
arr1 = []
arr2 = [0]*n
arr3 = []
for _ in range(n):
    x = input()
    if x not in arr1:
        arr1.append(x)
        arr2[arr1.index(x)] += 1
    else:
        arr2[arr1.index(x)] += 1
arr2 = set(arr2)
max_count = max(list(arr2.values()))
ans = []
for item in arr2.items():
    (key, value) = item
    if value == max_count:
        arr3.append(key)
arr3.sort()
for j in arr3:
    print(j)
"""
n = int(input())
s = [input() for _ in range(n)]
count = {}
for word in s:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1
max_count = max(list(count.values()))
ans = []
for item in list(count.items()):
    (key, value) = item
    if value == max_count:
        ans.append(key)
ans = sorted(ans)
for w in ans:
    print(w)
