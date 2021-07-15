from collections import defaultdict
from heapq import heappush, heappop, heapify
def main():
    N = int(input())
    SC = []
    SCrev = []
    for _ in range(N):
        s, c = input().split()
        c = int(c)
        SC.append((s, c))
        SCrev.append((s[::-1], c))
    dist = defaultdict(lambda: 10**18)
    q = [(c, s, "") for s, c in SC] + [(c, "", s) for s, c in SCrev]
    for c, l, r in q:
        dist[(l, r)] = min(dist[(l, r)], c)
    heapify(q)
    while q:
        dist_v, vl, vr = heappop(q)
        if (vl == vr == "") or (len(vl) and vl == vl[::-1]) or (len(vr) and vr == vr[::-1]):
            print(dist_v)
            return
        if dist[(vl, vr)] != dist_v:
            continue
        if len(vl) < len(vr):
            for s, c in SC:
                if len(s) <= len(vr):
                    if vr.startswith(s):
                        vr_ = vr[len(s):]
                        dist_u = dist_v + c
                        if dist_u < dist[("", vr_)]:
                            dist[("", vr_)] = dist_u
                            heappush(q, (dist_v+c, "", vr_))
                else:
                    if s.startswith(vr):
                        vl_ = s[len(vr):]
                        dist_u = dist_v + c
                        if dist_u < dist[(vl_, "")]:
                            dist[(vl_, "")] = dist_u
                            heappush(q, (dist_v+c, vl_, ""))
        else:
            for s, c in SCrev:
                if len(s) <= len(vl):
                    if vl.startswith(s):
                        vl_ = vl[len(s):]
                        dist_u = dist_v + c
                        if dist_u < dist[(vl_, "")]:
                            dist[(vl_, "")] = dist_u
                            heappush(q, (dist_v+c, vl_, ""))
                else:
                    if s.startswith(vl):
                        vr_ = s[len(vl):]
                        dist_u = dist_v + c
                        if dist_u < dist[("", vr_)]:
                            dist[("", vr_)] = dist_u
                            heappush(q, (dist_v+c, "", vr_))
    print((-1))

main()

