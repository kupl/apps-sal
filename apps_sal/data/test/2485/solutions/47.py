from collections import defaultdict,Counter

h,w,m = map(int,input().split())

w_list = []
h_list = []

se = set()

for _ in range(m):
    nh,nw = map(int,input().split())

    se.add((nh,nw))
    w_list.append(nw)
    h_list.append(nh)

w_count = Counter(w_list)
h_count = Counter(h_list)

max_w = 0
max_h = 0

ch = []
cw = []

for i in w_count.values():
    max_w = max(max_w,i)
    cw.append(i)

for i in h_count.values():
    max_h = max(max_h,i)
    ch.append(i)

ma = ch.count(max_h)*cw.count(max_w)

result = max_h+max_w
point = 0

for i,j in se:
    if w_count[j] == max_w and h_count[i] == max_h:
        point += 1

if point == ma:
    print(result-1)
else:
    print(result)
