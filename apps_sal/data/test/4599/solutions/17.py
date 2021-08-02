def ans088(N: int, a: str):
    a = list(map(int, a.split()))
    list.sort(a, reverse=True)
    Alice_count = 0
    Bob_count = 0
    for i in range(len(a)):
        if (i + 1) % 2 == 1:
            Alice_count += a[i]
        else:
            Bob_count += a[i]
    return Alice_count - Bob_count


N = int(input())
a = input()
print((ans088(N, a)))
