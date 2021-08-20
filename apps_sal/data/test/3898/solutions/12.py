def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(solver(a, b))


def solver(a, b):
    a.remove(0)
    b.remove(0)
    index = b.index(a[0])
    if b[index:] + b[:index] == a:
        return 'YES'
    else:
        return 'NO'


main()
