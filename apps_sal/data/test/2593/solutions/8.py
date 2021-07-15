for _ in range(int(input())):
    n = int(input())
    # s = input()
    # n,m = map(int,input().split())
    ar = list(map(int,input().split()))
    ar.sort()
    ans = 0
    t = []
    for i in range(n):
        t.append(len(bin(ar[i])[2:]))
    i = 0
    last = 0 
    count = 0 
    while i<n:
        if last==t[i]:
            count += 1
        else:
            ans += (count*(count+1))//2
            last = t[i]
            count = 0
        i += 1
    ans += (count*(count+1))//2
    # print(t)
    print(ans)
