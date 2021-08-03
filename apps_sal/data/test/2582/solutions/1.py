n = int(input())
ns = [int(x) for x in input().split()]
# n=200000
# ns=[x+1 for x in range(n)]

"""
st=[[ns[i]]for i in range(n)]
for l in range(1,20):
    for i in range(0,n+10,2**l):
        if i+2**(l-1)<len(st):
            st[i].append(max(st[i][-1],st[i+2**(l-1)][-1]))
def get_sum(l,r):
    ans,i=st[l][0],1
    while l+2**i<=r and i<len(st[l]):
        ans=st[l][i]
        i+=1
    rr=l+2**(i-1)-1
    if rr>=r:
        return ans
    else:
        return max(ans,get_sum(rr+1,r))
"""
# print(time.time()-tm)
# import random as rd
#
# n=10000
# s=set()
# ns=[]
# for i in range(n):
#     s.add(i+1)
# for i in range(n):
#     x=rd.sample(s,1)
#     ns.append(x[0])
#     s.remove(x[0])
# print(ns)
# quit()
# ns=[5, 8, 4, 1, 6, 7, 2, 3]
# n=len(ns)

maxx = max(ns) + 10
lst = [None] * n
nxt = [None] * n
tmp = [(-1, maxx)]
mp = [False] * n
wh = [None] * (n + 1)
for i in range(n):
    c = ns[i]
    while tmp[-1][1] <= c:
        tmp.pop()
    lst[i] = tmp[-1][0]
    tmp.append((i, c))
tmp = [(n, maxx)]
for i in range(n):
    i = n - i - 1
    c = ns[i]
    while tmp[-1][1] <= c:
        tmp.pop()
    nxt[i] = tmp[-1][0]
    tmp.append((i, c))
lm = {}
for i in range(n):
    lm[(lst[i] + 1, nxt[i] - 1)] = ns[i]
# print(lm)


for i in range(n):
    wh[ns[i]] = i


def check(i, m, lm):
    f = ns[m] - ns[i]
    f = wh[f]
    if lm[0] <= f <= lm[1]:
        return True
    return False


# print(wh)
ans = 0
rec = [(0, n - 1)]


def get():
    if len(rec) == 0:
        return False
    l, r = rec.pop()
    if r - l + 1 <= 2:
        return True
    nonlocal ans
    x = lm[(l, r)]
    lc = wh[x]
    if lc < (l + r) // 2:
        for i in range(l, lc):
            c = ns[i]
            c = ns[lc] - c
            c = wh[c]
            if lc <= c <= r:
                ans += 1
    else:
        for i in range(lc + 1, r + 1):
            c = ns[i]
            c = ns[lc] - c
            c = wh[c]
            if l <= c <= lc:
                ans += 1
    rec.append((l, lc - 1))
    rec.append((lc + 1, r))


while len(rec) > 0:
    get()
print(ans)
quit()


get(0, n - 1)
print(ans)
quit()


x = n
while x >= 1:
    lc = wh[x]
    mp[lc] = True
    l, r = lc - 1, lc + 1
    while l > lst[lc] and (not mp[l]):
        l -= 1
    while r < nxt[lc] and (not mp[r]):
        r += 1
    if lc - l < r - lc:
        for i in range(l + 1, lc):
            if check(i, lc, (lc + 1, r - 1)):
                ans += 1
    else:
        for i in range(lc + 1, r):
            if check(i, lc, (l + 1, lc - 1)):
                ans += 1
    x -= 1
print(ans)
#
# # print(lst)
# # print(nxt)
#
# def std(n,ns):
#     ans=0
#     for i in range(n):
#         for j in range(i,n):
#             if max(ns[i:j+1])==ns[i]+ns[j]:
#                 ans+=1
#     return ans
# print(ns)
# print(std(n,ns))
#
# if ans==std(n,ns):
#     print('True')
# else:
#     print('False')
