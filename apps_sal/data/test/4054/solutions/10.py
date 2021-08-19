a = list(map(int, input().split(' ')))
b = [1, 1, 2, 7, 4]
for i in range(len(a)):
    a[i] = a[i] // b[i]
r = min(a)
print(r)
