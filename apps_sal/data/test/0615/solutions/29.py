N = int(input())
alist = list(map(int, input().split()))

slist = []
asum = 0
for a in alist:
    asum += a
    slist.append(asum)
# print(alist)
# print(slist)

dic_lp, dic_rp = {}, {}
lp, rp = 0, 2
for mp in range(1, N - 2):
    # p1
    mindiff = slist[mp]
    while(lp < mp + 1):
        sum1 = slist[lp]
        sum2 = slist[mp] - slist[lp]

        diff = abs(sum1 - sum2)
        if mindiff > diff:
            lp += 1
            mindiff = diff
        else:
            lp -= 1
            dic_lp[mp] = lp
            # print(mp,lp)
            break

    rp = max(rp, mp + 1)
    mindiff = slist[-1] - slist[mp]
    while(rp < N):
        sum1 = slist[-1] - slist[rp]
        sum2 = slist[rp] - slist[mp]

        diff = abs(sum1 - sum2)
        if mindiff > diff:
            rp += 1
            mindiff = diff
        else:
            rp -= 1
            dic_rp[mp] = rp
            # print(mp,rp)
            break

min_diff = 10**9
for mp in range(1, N - 2):
    lp = dic_lp[mp]
    rp = dic_rp[mp]

    sum1 = slist[lp]
    sum2 = slist[mp] - slist[lp]
    sum3 = slist[rp] - slist[mp]
    sum4 = slist[-1] - slist[rp]
    # print(sum1,sum2,sum3,sum4)

    sum_list = [sum1, sum2, sum3, sum4]
    sum_list.sort()
    diff = sum_list[-1] - sum_list[0]
    # print(lp,mp,rp,diff)
    if diff < min_diff:
        min_diff = diff
        # print(min_diff)

print(min_diff)
