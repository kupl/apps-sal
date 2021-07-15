for _ in range(int(input())):
    s = input()
    p = [i for i in s.split("0") if i!=""]
    p.sort(reverse=True)
    ans = 0
    for i in range(0,len(p),2):
        ans+=len(p[i])
    print(ans)


