def go():
    n = int(input())
    a = sorted((int(i) for i in input().split(' ')))
    if n % 2 == 1:
        return a[n // 2]
    else:
        return a[n // 2 - 1]


print(go())
