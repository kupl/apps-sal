for _ in range(int(input())):
    n = int(input())
    ans = -1
    l = set(map(int, input().split()))
    for i in range(1, 4 * (10 ** 3)):
        s1 = set()
        for j in l:
            s1.add(i ^ j)
        if(s1 == l):
            ans = i
            break
    print(ans)
