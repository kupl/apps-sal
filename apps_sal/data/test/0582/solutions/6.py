

import sys

inp = sys.stdin.readline
def input(): return inp().strip()


def iin(): return int(input())


def lin(): return list(map(int, input().split()))


def main():
    import heapq as hq
    n = iin()
    a = lin()
    t = lin()
    dc = {}
    for i in range(n):
        try:
            dc[a[i]].append(t[i])
        except:
            dc[a[i]] = [t[i], ]
    sa = list(dc.keys())
    sa.sort()
    n = len(sa)
    ch = 0
    pt = sa[ch]
    temp = []
    sm = 0
    ans = 0
    hq.heapify(temp)
    done = 0
    while ch < n:
        pt = sa[ch]
        if len(dc[pt]) > 1 or done:
            a1 = sorted(dc[pt])
            for item in a1:
                hq.heappush(temp, -item)
                sm += item
            x = hq.heappop(temp) * (-1)
            dc[pt] = [x]
            sm -= x
            while len(temp):
                ans += sm
                pt += 1
                if pt in dc:
                    ch += 1
                    done = 1
                    break
                else:
                    x = hq.heappop(temp) * (-1)
                    sm -= x
            else:
                done = 0
        else:
            ch += 1
            done = 0
    print(ans)


main()
