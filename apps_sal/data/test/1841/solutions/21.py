(n, m) = [int(i) for i in input().split()]
sequence = list(map(int, input().split()))
l_list = [int(input()) - 1 for _ in range(m)]
max_num = max(sequence)
f = [0] * (max_num + 1)
k = 0
d = [0] * len(sequence)
for i in range(len(sequence) - 1, -1, -1):
    index = sequence[i]
    if f[index] == 0:
        f[index] = 1
        k += 1
    d[i] = k
for i in l_list:
    print(d[i])
