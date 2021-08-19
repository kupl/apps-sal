def main():
    n = int(input())
    sumtop = 0
    sumbottom = 0
    flippable = False
    for i in range(n):
        st = input()
        arr = st.split(' ')
        a = int(arr[0])
        b = int(arr[1])
        sumtop += a
        sumbottom += b
        if a % 2 + b % 2 == 1:
            flippable = True
    if sumtop % 2 == 0 and sumbottom % 2 == 0:
        print(0)
    elif sumtop % 2 + sumbottom % 2 == 1:
        print(-1)
    elif flippable:
        print(1)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
