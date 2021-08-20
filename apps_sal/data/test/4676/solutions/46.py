odd = list(map(str, input()))
even = list(map(str, input()))
if len(odd) == len(even):
    L = len(odd) * 2
else:
    L = len(odd) + len(even)
li = []
for i in range(1, L + 1):
    if i % 2 == 1:
        if i == 1:
            li.append(odd[0])
        else:
            li.append(odd[i // 2])
    else:
        li.append(even[i // 2 - 1])
print(''.join(li))
