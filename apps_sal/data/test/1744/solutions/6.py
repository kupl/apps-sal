#  author: ThePonyCoder
#  created: 19.06.2019, 17:45
#  filename: a.py
#  path: C:/Users/User/Desktop/python/Prog/CodeForces/rounds/cf_568/a.py

def ri():
    return [int(i) for i in input().split()]


def fl(a, b):
    return abs(a - b)


def gt_mx(d, l):
    ans = 0
    for i in reversed(range(1, 110)):
        if(l < 0):
            break
        if d[i] > 0:
            do = min(l // i, d[i])
            ans += do
            l -= do * i
            if l > 0 and do < d[i]:
                l -= i
                ans += 1
    
    return ans


def main(n, m, t):
    if m >= t[0]:
        print(0, end=' ')
    else:
        print(1, end=' ')
    d = {i: 0 for i in range(1, 110)}
    d[t[0]] += 1
    sm = t[0]
    for i in range(1, len(t)):
        sm += t[i]
        if i == 5:
            asd = 123
        if sm > m:
            delit = gt_mx(d, sm - m)
            print(delit, end=' ')
        else:
            print(0, end=' ')
        d[t[i]] += 1
        
        # print(ans, )
    # return ans


n, m = ri()
t = ri()
main(n, m, t)

