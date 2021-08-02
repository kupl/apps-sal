n = int(input())
a = [0] * n


def fun(n, ptr1):
    nonlocal a

    if n == 1:
        a[ptr1] = 1

    elif n == 2:

        a[ptr1] = 1
        ptr1 += 1
        a[ptr1] = 2
    elif n == 3:
        a[ptr1] = 1
        ptr1 += 1
        a[ptr1] = 1
        ptr1 += 1
        a[ptr1] = 3

    else:
        itera = n - n // 2

        for i in range(itera):
            a[ptr1] = 1
            ptr1 += 1

        fun(n // 2, ptr1)
        for i in range((n // 2)):
            a[ptr1] = 2 * a[ptr1]
            ptr1 += 1


fun(n, 0)
for i in a:
    print(i, end=" ")

print()
