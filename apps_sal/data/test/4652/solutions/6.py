for q in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    idx = a.index(1)

    b = a[idx:] + a[: idx]
    c = a[: idx + 1][::-1] + a[idx + 1:][::-1]

    a.sort()

    if b == a or c == a:
        print("YES")
    else:
        print("NO")
