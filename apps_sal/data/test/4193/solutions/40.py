def main():
    a = [list(map(int, input().split())) for _ in range(3)]
    n = int(input())
    b = [int(input()) for _ in range(n)]
    if a[0][0] in b and a[0][1] in b and a[0][2] in b or \
        a[1][0] in b and a[1][1] in b and a[1][2] in b or \
            a[2][0] in b and a[2][1] in b and a[2][2] in b or \
                a[0][0] in b and a[1][0] in b and a[2][0] in b or \
                    a[0][1] in b and a[1][1] in b and a[2][1] in b or \
                        a[0][2] in b and a[1][2] in b and a[2][2] in b or \
                            a[0][0] in b and a[1][1] in b and a[2][2] in b or \
                                a[0][2] in b and a[1][1] in b and a[2][0] in b:
                                    print('Yes')
    else:
        print('No')
        
def __starting_point():
    main()
__starting_point()
