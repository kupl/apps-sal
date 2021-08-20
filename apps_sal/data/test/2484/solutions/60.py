from heapq import heapify, heappush, heappop
n = int(input())
a = [int(i) for i in input().split()]
p = 0
ans = 0
cc = 0
cs = 0
chk = []
heapify(chk)
for (i, ai) in enumerate(a):
    heappush(chk, (i, ai))
    cc = cc ^ ai
    cs += ai
    ans += 1
    if cc != cs:
        p += (ans - 1) * ans // 2
        while chk:
            (j, aj) = heappop(chk)
            ans -= 1
            cc = cc ^ aj
            cs -= aj
            if cc == cs:
                p -= (ans - 1) * ans // 2
                cnt = 0
                break
p += ans * (ans + 1) // 2
print(p)
