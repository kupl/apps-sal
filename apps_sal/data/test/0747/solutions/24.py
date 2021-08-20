(n, x) = map(int, input().split())
count = 0
ans = 0
curr = 0
fruit = []
caramel = []
for i in range(n):
    (t, h, m) = map(int, input().split())
    if t == 0:
        caramel.append((h, m))
    else:
        fruit.append((h, m))
caramel = sorted(caramel)
fruit = sorted(fruit)
fruit2 = fruit[:]
caramel2 = caramel[:]
x2 = x


def add_to_mass(arr, x):
    candy = 0
    curr = 0
    for i in range(len(arr)):
        if arr[i][0] <= x:
            if arr[i][1] >= candy:
                candy = arr[i][1]
                curr = i
    if candy == 0:
        return 0
    arr.pop(curr)
    return candy


while True:
    curr = add_to_mass(fruit, x)
    if curr == 0:
        break
    else:
        x += curr
    count += 1
    curr = add_to_mass(caramel, x)
    if curr == 0:
        break
    else:
        x += curr
    count += 1
ans = count
count = 0
while True:
    curr = add_to_mass(caramel2, x2)
    if curr == 0:
        break
    else:
        x2 += curr
    count += 1
    curr = add_to_mass(fruit2, x2)
    if curr == 0:
        break
    else:
        x2 += curr
    count += 1
ans = max(count, ans)
print(ans)
