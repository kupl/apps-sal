t = int(input())
ret = []
while t > 0:
    t -= 1
    n, k, d1, d2 = map(int, input().split())

    # ans = []

    y1 = (k - (d1 - d2)) // 3
    x1 = y1 + d1
    z1 = y1 - d2
    # ans = [y1,z1,x1]
    # ans = sorted(ans)
    # ans1 = 2*ans[2]-(ans[0]+ans[1])
    ans1 = 2 * x1 - (z1 + y1)
    if x1 + y1 + z1 == k and min(z1, y1) >= 0 and ans1 <= n - k and (n - k - ans1) % 3 == 0:
        ret.append('yes')
        continue

    # ans = []

    y1 = (k - (d1 + d2)) // 3
    x1 = y1 + d1
    z1 = y1 + d2
    if d1 >= d2:
        # ans = [y1,z1,x1]
        ans1 = 2 * x1 - (y1 + z1)
    else:
        # ans = [y1,x1,z1]
        ans1 = 2 * z1 - (y1 + x1)
    # ans = sorted(ans)
    # ans1 = 2*ans[2]-(ans[0]+ans[1])
    if x1 + y1 + z1 == k and y1 >= 0 and ans1 <= n - k and (n - k - ans1) % 3 == 0:
        ret.append('yes')
        continue

    y1 = (k - (d2 - d1)) // 3
    x1 = y1 - d1
    z1 = y1 + d2
    # ans = [x1,y1,z1]
    # ans = sorted(ans)
    ans1 = 2 * z1 - (x1 + y1)
    if x1 + y1 + z1 == k and min(x1, y1) >= 0 and ans1 <= n - k and (n - k - ans1) % 3 == 0:
        ret.append('yes')
        continue

    y1 = (k + (d2 + d1)) // 3
    x1 = y1 - d1
    z1 = y1 - d2
    # ans = [x1,y1,z1]
    # ans = sorted(ans)
    ans1 = 2 * y1 - (x1 + z1)
    if x1 + y1 + z1 == k and min(x1, z1) >= 0 and ans1 <= n - k and (n - k - ans1) % 3 == 0:
        ret.append('yes')
        continue

    # if d1>=d2:
    #     ans.append(2*d1-d2)
    #     ans.append(d2+2*(d1-d2))
    # else:
    #     ans.append(2*d2-d1)
    #     ans.append(d1+2*(d2-d1))

    # ans+=[d1+2*d2,d2+2*d1,d1+d2]
    # done = False
    # print(ans)
    # for a in ans:
    #     # if (a==0 and (n-k)%3==0) or (a!=0 and (n-k)//a>1 and (n-k)%a==0):
    #     if (a<=n-k) and (n-k-a)%3==0:
    #         print(a)
    #         done = True
    #         break

    # if done:
    #     print('yes')
    # else:
    ret.append('no')

print(*ret, sep='\n')
