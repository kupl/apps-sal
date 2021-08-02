n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
diz = {}
for i in range(n - 1):
    for j in range(i + 1, n):
        appo = (array[i] + array[j])
        if appo % 2 == 0:
            diz[appo >> 1] = 1
counter = 0
for el in array:
    if el in diz:
        counter += 1
print(counter)
