(n, k) = map(int, input().split())
bin_ = list(map(int, input().split()))
sorted_bin = []
command = [0] * n
next_ = [i for i in range(1, n)] + [-1]
prev_ = [-1] + [i for i in range(0, n - 1)]
for elem in enumerate(bin_):
    sorted_bin.append(elem)
sorted_bin.sort(key=lambda x: -x[1])
flag = 0
for (ind, value) in sorted_bin:
    if command[ind] != 0:
        continue
    command[ind] = flag + 1
    next_i = ind
    for _ in range(k):
        next_i = next_[next_i]
        if next_i != -1:
            command[next_i] = 1 + flag
        else:
            break
    prev_i = ind
    for _ in range(k):
        prev_i = prev_[prev_i]
        if prev_i != -1:
            command[prev_i] = 1 + flag
        else:
            break
    if prev_i != -1:
        prev_i = prev_[prev_i]
    if next_i != -1:
        next_i = next_[next_i]
    if prev_i != -1:
        next_[prev_i] = next_i
    if next_i != -1:
        prev_[next_i] = prev_i
    flag = 1 - flag
for i in command:
    print(i, end='')
