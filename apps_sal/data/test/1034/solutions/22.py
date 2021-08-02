import heapq
x, y, z, k = map(int, input().split())
alist = sorted(list(map(int, input().split())), reverse=True)
blist = sorted(list(map(int, input().split())), reverse=True)
clist = sorted(list(map(int, input().split())), reverse=True)
l = [(-(alist[0] + blist[0] + clist[0]), 0, 0, 0)]
heapq.heapify(l)
count = 0
ai = bi = ci = 0
selected = set()
selected.add((0, 0, 0))
while len(l) != 0:
    temp = heapq.heappop(l)
    (tempa, tempb, tempc) = temp[1:]
    print(-temp[0])
    count += 1
    if count == k:
        break
    if tempa + 1 <= x - 1:
        if not (tempa + 1, tempb, tempc) in selected:
            heapq.heappush(l, (-(alist[tempa + 1] + blist[tempb] + clist[tempc]), tempa + 1, tempb, tempc))
            selected.add((tempa + 1, tempb, tempc))
    if tempb + 1 <= y - 1:
        if not (tempa, tempb + 1, tempc) in selected:
            heapq.heappush(l, (-(alist[tempa] + blist[tempb + 1] + clist[tempc]), tempa, tempb + 1, tempc))
            selected.add((tempa, tempb + 1, tempc))
    if tempc + 1 <= z - 1:
        if not (tempa, tempb, tempc + 1) in selected:
            heapq.heappush(l, (-(alist[tempa] + blist[tempb] + clist[tempc + 1]), tempa, tempb, tempc + 1))
            selected.add((tempa, tempb, tempc + 1))
