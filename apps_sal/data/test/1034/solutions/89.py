from heapq import heappop, heappush

x, y, z, k = [int(i) for i in input().split()]

a_list = sorted([-int(i) for i in input().split()])
b_list = sorted([-int(i) for i in input().split()])
c_list = sorted([-int(i) for i in input().split()])

hq = []
flag_set = set()

heappush(hq, (a_list[0] + b_list[0] + c_list[0], 0, 0, 0))
flag_set.add((0, 0, 0))
for _ in range(k):
    d, ai, bi, ci = heappop(hq)
    print(-d)
    
    temp = (ai + 1, bi, ci)
    if temp[0] < x and temp not in flag_set:
        heappush(hq, (a_list[ai + 1] + b_list[bi] + c_list[ci], ai + 1, bi, ci))
        flag_set.add(temp)
    
    temp = (ai, bi + 1, ci)
    if temp[1] < y and temp not in flag_set:
        heappush(hq, (a_list[ai] + b_list[bi + 1] + c_list[ci], ai, bi + 1, ci))
        flag_set.add(temp)

    temp = (ai, bi, ci + 1)
    if temp[2] < z and temp not in flag_set:
        heappush(hq, (a_list[ai] + b_list[bi] + c_list[ci + 1], ai, bi, ci + 1))
        flag_set.add(temp)
