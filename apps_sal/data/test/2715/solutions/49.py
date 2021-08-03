k = int(input())
v = [i + (k // 50) for i in range(50)]
for i in range(k % 50):
    for j in range(50):
        if i == j:
            v[j] += 50
            continue
        v[j] -= 1
print(50)
print(*v)
