from heapq import heappop,heappush
l = []
r = []
Q = int(input())
ans = 0
l_s = 0
r_s = 0
_,m,b = map(int,input().split())
ans += b
n = 0
for i in range(1,Q):
    s = input()
    if s != '2':
        _,a,b = map(int,s.split())
        ans += b
        if n == 0:
            c,d = sorted([m,a])
            heappush(l,-c)
            heappush(r,d)
            l_s += c
            r_s += d
            m1 = c
        else:
            c,d = heappop(l),heappop(r)
            l_s += c
            r_s -= d
            c = -c
            if n%2 == 1:
                c,m,d = sorted([a,c,d])
                heappush(l,-c)
                heappush(r,d)
                l_s += c
                r_s += d
            else:
                c,m1,m2,d = sorted([m,a,c,d])
                heappush(l,-c)
                heappush(l,-m1)
                heappush(r,d)
                heappush(r,m2)
                l_s += c
                r_s += d
                l_s += m1
                r_s += m2
        n += 1
    else:
        if n == 0:
            print('{} {}'.format(m,ans))
        elif n == 1:
            print('{} {}'.format(m1,r_s-l_s+ans))
        elif n%2 == 0:
            print('{} {}'.format(m,r_s-l_s+ans))
        else:
            print('{} {}'.format(m1,r_s-l_s+ans))
