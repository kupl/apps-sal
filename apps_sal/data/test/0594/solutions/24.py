def main():
    (n, m) = [int(item) for item in input().split()]
    A = [int(item) for item in input().split()]
    B = [int(item) for item in input().split()]
    x = max(2 * min(A), max(A))
    y = min(B)
    if x < y:
        print(x)
    else:
        print('-1')


main()
