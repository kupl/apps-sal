from collections import Counter

N = input()
list1 = list(map(int, input().split()))
dict1 = Counter(list1)

key1 = list(dict1.keys())
value1 = list(dict1.values())

ans = 0
for i in range(len(key1)):
    x = value1[i]
    y = key1[i]
    if x >= y:
        ans += x - y
    else:
        ans += x

print(ans)
