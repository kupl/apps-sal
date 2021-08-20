from collections import Counter
(h, w, m) = list(map(int, input().split()))
h = []
w = []
for i in range(m):
    (h_, w_) = list(map(int, input().split()))
    h.append(h_)
    w.append(w_)
dic_h = Counter(h)
dic_w = Counter(w)
max_h = max(dic_h.values())
max_w = max(dic_w.values())
h_set = set()
w_set = set()
for i in dic_h:
    if dic_h[i] == max_h:
        h_set.add(i)
for j in dic_w:
    if dic_w[j] == max_w:
        w_set.add(j)
cnt = 0
for i in range(m):
    if h[i] in h_set and w[i] in w_set:
        cnt += 1
if len(h_set) * len(w_set) > cnt:
    print(max_h + max_w)
else:
    print(max_h + max_w - 1)
