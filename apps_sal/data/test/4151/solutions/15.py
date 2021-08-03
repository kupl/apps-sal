def step(x):
    ans = 1
    for i in range(x):
        ans = (ans * 2) % 998244353
    return ans


n = int(input())
arr = input().split()
arr = list(map(lambda x: int(x), arr))
counter = 0
first = {}
last = {}
for x in range(len(arr)):
    if (arr[x] not in first):
        first[arr[x]] = x
        last[arr[x]] = x
    else:
        last[arr[x]] = x
arr2 = [0] * n
for x in first:
    arr2[first[x]] += 1
    arr2[last[x]] -= 1
sum = 0
for i in arr2:
    if (sum == 0):
        counter += 1
    sum += i
counter -= 1
print(step(counter))
