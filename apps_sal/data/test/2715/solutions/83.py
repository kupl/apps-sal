k = int(input())

a = [49 + k // 50] * 50

b = k % 50

if b:
    for i in range(50):
        if i < b:
            a[i] += 50 - (b-1)
        else:
            a[i] -= b

print((50))
print((" ".join(list(map(str, a)))))

