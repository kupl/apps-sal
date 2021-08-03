def main():
    n = int(input())

    b = [int(x) for x in input().split()]

    if len(b) == 1:
        if b[0] == 0:
            print("NO")
        else:
            print("YES")
    else:
        flag = False

        for x in b:
            if x == 0:
                if not flag:
                    flag = True
                else:
                    print("NO")
                    return
        if flag:
            print("YES")
        else:
            print("NO")


main()
