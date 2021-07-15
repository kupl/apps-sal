n,x = map(int,input().split())
k = [[],[]]
def add(s):
    t,h,m = map(int,s.split())
    k[t].append([h,m])
[add(input()) for _ in range(n)]
def calc(t):
    cur = x
    ans = 0
    mark = [[False] * len(k[0]),[False] * len (k[1])]
    while True:
        w = 0
        id = 0
        for i in range(len(k[t])):
            if mark[t][i] == False and w < k[t][i][1] and cur >= k[t][i][0]:
                w = k[t][i][1]
                id = i
        if w == 0: break
        ans += 1
        cur += w
        mark[t][id] = True
        t = 1 - t
    return ans
sol = max(calc(0),calc(1))
print (sol)
