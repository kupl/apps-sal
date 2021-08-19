t = int(input())
while t > 0:
    ans = 0
    n, m = [int(x) for x in input().split()]
    a = []
    nn = n
    while nn > 0:
        a.append(input())
        nn -= 1
    for i in range(n):
        for j in range(n):
            if a[i][j] == "X":
                c = i
                d = j
                r = 0
                p = 0
                q = 0
                while c < n and ((a[c][d] == "X" or a[c][d] == ".") and q < 2):
                    if a[c][d] != "X":
                        if p == 0:
                            p = r

                        q += 1
                    r += 1
                    c += 1
                if r >= m:
                    ans = 1

                c = i
                d = j
                r1 = 0
                p1 = 0
                q = 0
                while c >= 0 and ((a[c][d] == "X" or a[c][d] == ".") and q < 2):
                    if a[c][d] != "X":
                        if p1 == 0:
                            p1 = r1

                        q += 1
                    r1 += 1
                    c -= 1
                if r1 >= m:
                    ans = 1

                c = i
                d = j
                r = 0
                p = 0
                q = 2
                while d < n and ((a[c][d] == "X" or a[c][d] == ".") and q < 2):
                    if a[c][d] != "X":
                        if p == 0:
                            p = r
                        q += 1

                    r += 1
                    d += 1
                if r >= m:
                    ans = 1

                c = i
                d = j
                r1 = 0
                p1 = 0
                q = 0
                while d >= 0 and ((a[c][d] == "X" or a[c][d] == ".") and q < 2):
                    if a[c][d] != "X":
                        if p1 == 0:
                            p1 = r1
                        q += 1
                    r1 += 1
                    d -= 1
                if r1 >= m:
                    ans = 1

                c = i
                d = j
                r = 0
                p = 0
                q = 0
                while d < n and c < n and ((a[c][d] == "X" or a[c][d] == ".") and q < 2):
                    if a[c][d] != "X":
                        if p == 0:
                            p = r
                        q += 1
                    r += 1
                    d += 1
                    c += 1
                if r >= m:
                    ans = 1

                c = i
                d = j
                r1 = 0
                p1 = 0
                q = 0
                while d >= 0 and c >= 0 and ((a[c][d] == "X" or a[c][d] == ".") and q < 2):
                    if a[c][d] != "X":
                        if p1 == 0:
                            p1 = r1
                        q += 1
                    r1 += 1
                    d -= 1
                    c -= 1
                if r1 >= m:
                    ans = 1

                # if i==0 and j==0:
                #    print(str(r1)+" "+str(p1)+" "+str(r)+" "+str(p))

                c = i
                d = j
                r = 0
                p = 0
                q = 0
                while d < n and c >= 0 and ((a[c][d] == "X" or a[c][d] == ".") and q < 2):
                    if a[c][d] != "X":
                        if p == 0:
                            p = r
                        q += 1
                    r += 1
                    d += 1
                    c -= 1
                if r >= m:
                    ans = 1

                c = i
                d = j
                r1 = 0
                p1 = 0
                q = 0
                while d >= 0 and c < n and ((a[c][d] == "X" or a[c][d] == ".") and q < 2):
                    if a[c][d] != "X":
                        if p1 == 0:
                            p1 = r1
                        q += 1
                    r1 += 1
                    d -= 1
                    c += 1
                if r1 >= m:
                    ans = 1

    if m == 1:
        ans = 1
    if ans == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
