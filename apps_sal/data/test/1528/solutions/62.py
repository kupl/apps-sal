a = [1]
b = [1]
for _ in range(50):
    a.append(2 * a[-1] + 3)
    b.append(2 * b[-1] + 1)

def num_of_patties(n, x):
    if n == 0:
        return 1

    if x == 1:
        return 0
    elif x <= a[n-1] + 1:
        return num_of_patties(n-1, x-1)
    elif x == a[n-1] + 2:
        return b[n-1] + 1
    elif x <= 2 * a[n-1] + 2:
        return b[n-1] + 1 + num_of_patties(n-1, x-a[n-1]-2)
    else:
        return b[n]


print((num_of_patties(*[int(i) for i in input().split()])))

