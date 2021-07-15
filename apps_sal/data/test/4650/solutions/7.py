t = int(input())
for l in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    co1 = 0
    co2 = 0
    co = 0
    for i in arr:
        if i%3==0:
            co += 1
        if i%3==1:
            co1 += 1
        if i%3==2:
            co2 += 1
    ans = co
    ans += min(co1,co2)
    left = max(co2,co1)-min(co2,co1)
    ans += int(left/3)
    print(ans)
