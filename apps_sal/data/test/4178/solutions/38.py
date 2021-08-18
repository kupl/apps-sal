

def main():
    _ = int(input())
    tmp = 1
    ans = 'Yes'
    H = list(map(int, input().split()))

    for h in H:
        if tmp < h:
            tmp = h - 1
        elif tmp > h:
            ans = 'No'
            break

    print(ans)


def __starting_point():
    main()


__starting_point()
