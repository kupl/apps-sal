counter = dict()
max_num = (0, 0)

n = int(input())
A = list(map(int, input().split()))

for i in range(len(A)):
    if A[i] in counter:
        counter[A[i]][0] += 1
        counter[A[i]][2] = i
    else:
        counter[A[i]] = [1, i, i]

count, l, r = max(list(counter.values()), key=lambda x: (x[0], -(x[2] - x[1]), -x[1]))
print(l + 1, r + 1)
