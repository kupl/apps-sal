n = int(input())
counter = 0
dic = {}
for i in range(n):
    a = list(input())
    if a[0] not in dic:
        dic[a[0]] = 1
    else:
        dic[a[0]] += 1
for item in dic:
    y = dic[item]
    x = dic[item] // 2
    counter += x * (x - 1) // 2 + (y - x) * (y - x - 1) // 2
print(counter)
