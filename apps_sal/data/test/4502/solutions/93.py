n = int(input())
A = list(input().split())

if (n - 1) % 2 == 0:
    top = [""] * ((n - 1) // 2)
    bottom = [""] * ((n - 1) // 2)

    t = (n - 1) // 2 - 1
    b = 0
    for i in range(1, n):
        if i % 2 == 1:
            bottom[b] = A[i]
            b += 1
        else:
            top[t] = A[i]
            t -= 1
else:
    top = [""] * ((n - 1) // 2 + 1)
    bottom = [""] * ((n - 1) // 2)

    t = (n - 1) // 2
    b = 0

    for j in range(1, n):
        if j % 2 == 1:
            top[t] = A[j]
            t -= 1
        else:
            bottom[b] = A[j]
            b += 1

print(*(top + [A[0]] + bottom))
