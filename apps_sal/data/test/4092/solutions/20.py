n = int(input())
A = [int(i) for i in input().split()]
cumm = [A[0]] * n
d = {A[0]: [0]}
count = 0
last_idx = -1
for i in range(1, n):
    cumm[i] = cumm[i - 1] + A[i]
    if cumm[i] == 0 and last_idx == -1:
        count += 1
        last_idx = i
    elif cumm[i] in d:
        l = d[cumm[i]]
        if l[-1] >= last_idx - 1:
            count += 1
            last_idx = i
    if cumm[i] not in d:
        d[cumm[i]] = []
    d[cumm[i]].append(i)
print(count)
