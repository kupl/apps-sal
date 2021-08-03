# alpha = "abcdefghijklmnopqrstuvwxyz"
from heapq import heappop, heappush
prime = 998244353
t = 1  # int(input())
for test in range(t):
    n = int(input())
    # n,m = (map(int, input().split()))
    s = input()
    # ans = 1
    # start = 1
    # cur = s[0]
    # tmp = 0
    # while s[start]==cur:
    #     start+=1
    #     tmp+=1
    # end = n-1
    # tmp = 1
    # while s[end]==cur:
    #     end-=1
    #     tmp+=1
    grp = []
    cnt = []
    tmp = 0
    cur = s[0]
    for i in s:
        if i == cur:
            tmp += 1
        else:
            grp.append(cur)
            cnt.append(tmp)
            cur = i
            tmp = 1
    grp.append(cur)
    cnt.append(tmp)
    if len(grp) == 1:
        print(((n * (n + 1)) // 2) % prime)
    else:
        if grp[0] == grp[-1]:
            ans = ((cnt[0] + 1) * (cnt[-1] + 1)) % prime
            # print("here", ans)
            # if cnt[0]+cnt[-1]==n-1:
            #     ans-=1
            #     ans = ans%prime
            print(ans)
        else:
            ans = cnt[0] + 1 + cnt[-1]
            ans = ans % prime
            # if cnt[0]+cnt[-1]==n-1:
            #     ans-=1
            #     ans = ans%prime
            print(ans)
