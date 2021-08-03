t = int(input())
while(t):
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    ans = a.count(0)
    summ = sum(a) + ans
    if(summ == 0):
        print(ans + 1)
    else:
        print(ans)
