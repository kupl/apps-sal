for kkk in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[l[i]] = i
    ans = ["0" for i in range(n + 1)]
    ans[1] = "1"
    posleft = d[1]
    posright = d[1]
    for j in range(2, n + 1):
        if(d[j] == posleft - 1 or d[j] == posright + 1):
            if(ans[j - 1] == "1"):
                ans[j] = "1"
        elif(d[j] < posright and d[j] > posleft):
            if(posright - posleft + 1 == j):
                ans[j] = "1"
        if(d[j] < posleft):
            posleft = d[j]
        if(d[j] > posright):
            posright = d[j]
    print(''.join(ans[1:]))
