import copy

n = int(input())
v = list(map(int, input().split()))
# print(v)

la = [0 for i in range(5+10**5)]
lb = [0 for i in range(5+10**5)]

for i in range(0, n, 2):
    la[v[i]] += 1
for i in range(1, n, 2):
    lb[v[i]] += 1

# print(sum(la))
# print(sum(lb))
# print(max(la))
# print(max(lb))
# print(la.index(max(la)))
# print(lb.index(max(lb)))

sla = sum(la)
slb = sum(lb)
maxla = max(la)
maxlb = max(lb)
argmaxla = la.index(max(la))
argmaxlb = lb.index(max(lb))

if argmaxla != argmaxlb:
    if sla-maxla == 0 and slb-maxlb == 0:
        print((0))
    else:
        print((sla-maxla+slb-maxlb))
else:
    # laの2番目に大きい値を使う
    _la = copy.deepcopy(la)
    _la[argmaxla] = 0
    _maxla = max(_la)
    aa = sla-_maxla+slb-maxlb
    # lbの2番目に大きい値を使う
    _lb = copy.deepcopy(lb)
    _lb[argmaxlb] = 0
    _maxlb = max(_lb)
    bb = sla-maxla+slb-_maxlb
    if bb > aa:
        print(aa)
    else:
        print(bb)

