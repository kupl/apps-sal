(n, m) = list(map(int, input().split()))
lst = []
for x in input().split():
    lst.append(int(x))
array = [0] * n
for x in range(len(lst)):
    array[lst[x] - 1] += 1
print(min(array))
