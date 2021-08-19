n = int(input())
a = list(map(int, input().split()))
sortedIndex = sorted(range(n), key=lambda k: a[k])
temp = 0
for i in range(n):
    if a[sortedIndex[i]] <= temp:
        a[sortedIndex[i]] = temp
        temp += 1
    elif a[sortedIndex[i]] > temp:
        temp = a[sortedIndex[i]] + 1
result = ' '.join((str(e) for e in a))
print(result)
