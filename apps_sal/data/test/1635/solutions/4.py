n = int(input())
arr = list(map(int, input().split()))
was = [10000000000000000000] * (2 * 10 ** 5 + 10)
for i in range(n):
    was[arr[i]] = i
mn = 10 ** 9
mn_i = -1
for el in arr:
    if was[el] < mn:
        mn = was[el]
        mn_i = el
print(mn_i)
