def solve():
    n = int(input())
    l = [[] for i in range(n + 1)]
    for i in range(2, n + 1):
        a = int(input())
        l[a].append(i)

    for i in l:
        if len(i) != 0:
            leafCount = 0
            for j in i:
                if len(l[j]) == 0:
                    leafCount += 1
            if leafCount < 3:
                print("No")
                return
    print("Yes")


solve()
