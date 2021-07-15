for T in range(int(input())) :
    n = int(input())
    l = list(map(int,input().split()))
    bal = 0 
    ans = 0
    for i in l :
        if i >= 0 :
            bal += i
        else :
            if abs(i) > bal :
                ans += abs(i)-bal
                bal = 0
            else :
                bal += i 
    print(ans)
