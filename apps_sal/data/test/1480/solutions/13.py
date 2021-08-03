n, k = [int(x) for x in str(input()).split(' ', 1)]
next_ = [i + 1 for i in range(n + 1)]
next_[n] = 1
a = [int(x) for x in str(input()).split(' ')]
remain = n
cur = 1
prev = None
eli = []
for a0 in a:
    a0 = a0 % remain
    for _ in range(a0):
        prev = cur
        # print("{}->{}".format(cur, next_[cur]))
        cur = next_[cur]
    if prev is None:
        prev = cur
        while next_[prev] != cur:
            prev = next_[prev]
    # print("====")
    eli.append(cur)
    next_[prev] = next_[cur]
    cur = next_[cur]
    remain -= 1
print(' '.join([str(e) for e in eli]))
