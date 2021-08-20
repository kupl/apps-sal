def get_input_list():
    return list(map(int, input().split()))


(n, k) = get_input_list()
h = get_input_list()
h.sort()
l = []
for i in range(n - 1, 0, -1):
    if h[i] != h[i - 1]:
        for _ in range(h[i] - h[i - 1]):
            l.append(n - i)
if len(l) == 0:
    print(0)
else:
    p = 0
    r = 1
    for i in l:
        if p + i <= k:
            p += i
        else:
            r += 1
            p = i
    print(r)
