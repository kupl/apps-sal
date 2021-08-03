try:
    n = int(input())
    l1 = [int(x) for x in input().split()]

    l2 = [int(x) for x in input().split()]
    ans = []
    t2 = -1
    for i in range(n):

        if(t2 <= l1[i]):
            ans.append(i)
            t2 = l2[i]

    for e in ans:
        print(e, end=' ')
except EOFError:
    pass
