from heapq import heappop, heappush
prime = 998244353
t = 1
for test in range(t):
    n = int(input())
    s = input()
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
            print(ans)
        else:
            ans = cnt[0] + 1 + cnt[-1]
            ans = ans % prime
            print(ans)
