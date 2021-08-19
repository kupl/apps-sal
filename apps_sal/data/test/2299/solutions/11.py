from sys import stdin
(n, m) = list(map(int, stdin.readline().rstrip().split()))
data = []
for i in range(0, n):
    data.append(list(map(int, stdin.readline().rstrip().split())))
sorted_data = [0] * n
for col in range(0, m):
    mark_r = 0
    cur_r = 1
    st = []
    while cur_r < n:
        if data[cur_r][col] < data[cur_r - 1][col]:
            st.extend([cur_r - 1] * (cur_r - mark_r))
            mark_r = cur_r
        cur_r += 1
    st.extend([cur_r - 1] * (cur_r - mark_r))
    for (index, item) in enumerate(st):
        if sorted_data[index] < st[index]:
            sorted_data[index] = st[index]
q_count = int(stdin.readline().rstrip())
for _ in range(0, q_count):
    (l, r) = [int(x) - 1 for x in stdin.readline().rstrip().split()]
    if sorted_data[l] >= r:
        print('Yes')
    else:
        print('No')
