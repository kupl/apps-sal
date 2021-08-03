for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d1 = {}
    for i in l:
        if i in d1:
            d1[i] += 1

        else:
            d1[i] = 1

    f = True
    li = []
    for i in d1:
        if d1[i] % 2 != 0:
            f = False
            break
        else:
            li.extend([i] * (d1[i] // 2))

    if f:
        li.sort()
        c = li[0] * li[-1]
        i = 1
        j = len(li) - 2
        while i < j:
            if c != li[i] * li[j]:
                f = False
                break

            else:
                i += 1
                j -= 1
        if f:
            print("YES")

        else:
            print("NO")

    else:
        print("NO")
