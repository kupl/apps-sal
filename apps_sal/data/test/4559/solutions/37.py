N = int(input())
A = list(map(int, input().split()))


def ans():
    if 0 in A:
        return print(0)
    product = 1
    for num in A:
        product = product * num
        if product > 10 ** 18:
            return print(-1)
    print(product)


ans()
