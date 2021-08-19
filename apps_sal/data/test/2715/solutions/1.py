k = int(input())

if k == 0:
    a = [1, 1]
elif k == 1:
    a = [2, 0]
elif k <= 50:
    a = [i for i in range(1, k + 1)]
else:
    a = [i for i in range(1, 51)]
    k -= 50
    d = k // 50
    for i in range(50):
        a[i] += d
    m = k % 50
    for i in range(-1, -m - 1, -1):
        a[i] += 1
print((len(a)))

# print(a)

a = [str(i) for i in a]
print((' '.join(a)))
