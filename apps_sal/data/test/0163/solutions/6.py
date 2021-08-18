def main():
    n, k = list(map(int, input().split()))
    a = input()
    l = 0
    r = 0
    for i in range(n):
        if (a[i] == 'G'):
            l = i
        elif (a[i] == 'T'):
            r = i
    if (l < r):
        if ((r - l) % k == 0):
            for i in range(l, r + 1, k):
                if (a[i] == '
                    print("NO")
                    return
            print("YES")
        else:
            print("NO")
    else:
        if ((r - l) % k == 0):
            for i in range(r, l + 1, k):
                if (a[i] == '
                    print("NO")
                    return
            print("YES")
        else:
            print("NO")


main()
