for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    ans1 = 0
    ans2 = [None] * n
    for j in range(n):
        if l[j] not in ans2:
            ans2[j] = l[j]
    for j in range(n):
        if ans2[j] == None:
            for pos in range(4):
                for d in range(9):
                    jd = l[j][:pos] + chr(ord('0') + d) + l[j][pos + 1:]
                    if jd not in ans2:
                        ans1 += 1
                        ans2[j] = jd
                        break
                else:
                    continue
                break
    print(ans1)
    for i in ans2:
        print(i)
