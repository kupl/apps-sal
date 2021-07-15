def main():
    n = int(input())
    a = [int(t) for t in input().split()]
    shift = n - a[0]

    turn = 1
    out = 'Yes'
    for i in range(len(a)):
        a[i] = (a[i] + turn * shift) % n
        turn *= -1
        if a[i] != i:
            out = 'No'
            break

    print(out)

def __starting_point():
    main()
__starting_point()
