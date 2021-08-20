(n, m) = map(int, input().split())
data = list(map(int, input().split()))
array = []
c = 0
for i in data:
    if i not in array:
        c += 1
        if c > m:
            array = [i] + array[:-1]
        else:
            array = [i] + array
print(m if c >= m else c)
print(*array)
