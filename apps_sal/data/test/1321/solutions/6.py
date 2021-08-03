__author__ = 'ruckus'

n = int(input())

w = [0 for i in range(n)]
h = [0 for i in range(n)]

max_w = 0
max_h = 0
premax_h = 0
in_w = []
in_h = []
for i in range(n):
    cur_w, cur_h = input().split()
    cur_h = int(cur_h)
    cur_w = int(cur_w)
    max_w += cur_w
    in_w.append(cur_w)
    in_h.append(cur_h)
max_h = max(in_h)
copy_in_h = in_h.copy()
copy_in_h.remove(max_h)
premax_h = max(copy_in_h)
for i in range(n):
    w[i] = max_w - in_w[i]
    if in_h[i] == max_h:
        h[i] = premax_h
    else:
        h[i] = max_h

for w, h in zip(w, h):
    print(w * h, end=' ')
