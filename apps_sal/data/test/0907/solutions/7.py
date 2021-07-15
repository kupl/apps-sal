import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))

number = [list(map(int, input().split())) for _ in range(m)]
a = number[0][0]
b = number[0][1]
if a > n and b > n:
    print("NO")
else:
    flaga1 = 1
    flaga2 = 1
    flagb1 = 1
    flagb2 = 1
    count = 0
    if a <= n:
        c = a
        d = a
        for i in number:
            if a not in i:
                c = i[0]
                d = i[1]
                break

        for i in number:
            if a not in i and d not in i:
                flaga1 = 0
                break


        for i in number:
            if a not in i and c not in i:
                flaga2 = 0
                break




    if b <= n:
        c = b
        d = b
        for i in number:
            if b not in i:
                c = i[0]
                d = i[1]
                break

        for i in number:
            if b not in i and d not in i:
                flagb1 = 0
                break


        for i in number:
            if b not in i and c not in i:
                flagb2 = 0
                break


    if flaga1 == 0 and flaga2 == 0 and flagb1 == 0 and flagb2 == 0:
        print("NO")
    else:
        print("YES")

