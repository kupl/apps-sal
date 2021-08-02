k = int(input())

tasu = k // 50
lst = list(range(tasu, tasu + 50))
amari = k % 50
for i in range(amari):
    idx = 49 - i
    lst[idx] += 1

print(50)
print(' '.join(map(str, lst)))
