n = int(input())
i = 0
w = [] * n
h = [] * n
i = 0
while (i < n):
    pair = input().split()
    w.append(int(pair[0]))
    h.append(int(pair[1]))
    i += 1
W = 0
for x in w:
    W += x
h_sorted = sorted(h)
for x in range(0, n):
    W_new = W - w[x]
    if(h[x] == h_sorted[-1]):
        h_new = h_sorted[-2]
    else:
        h_new = h_sorted[-1]
    b = h_new * W_new
    print(b, end=" ")
