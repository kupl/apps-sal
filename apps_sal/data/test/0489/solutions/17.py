n = int(input())
a = sorted(list(map(int,input().split())))
min1 = a[0];min2 = a[1];min3 = a[2]
t = True
if(min1 == min2 and min2 == min3):
    cnt = 0
    for i in a:
        if i == min1:
            cnt += 1
    cnt = cnt * (cnt-1) * (cnt-2)
    print(cnt // 6)
    t = False

if(min1 == min2 and t):
    cnt12 = 0
    cnt3 = 0
    for i in a:
        if i == min1:
            cnt12 += 1
        if i == min3:
            cnt3 += 1
    print((cnt12 * (cnt12 - 1) // 2 ) * cnt3)


if(min1 == min3 and t):
    cnt13 = 0
    cnt2 = 0
    for i in a:
        if i == min1:
            cnt13 += 1
        if i == min2:
            cnt2 += 1
    print((cnt13 * (cnt13 - 1) // 2 ) * cnt2)




if(min3 == min2 and t):
    cnt32 = 0
    cnt1 = 0
    for i in a:
        if i == min3:
            cnt32 += 1
        if i == min1:
            cnt1 += 1
    print((cnt32 * (cnt32 - 1) // 2 ) * cnt1)

if(min1 != min2 and min2 != min3 and min1 != min3):
    cnt1 = 0;cnt2 = 0;cnt3 = 0
    for i in a:
        if i == min1:cnt1+=1
        if i == min2:cnt2+=1
        if i == min3:cnt3+=1
    print(cnt1*cnt2*cnt3)

