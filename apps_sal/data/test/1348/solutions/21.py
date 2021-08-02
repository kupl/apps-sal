n, k = input().split()
n = int(n)
k = int(k)

d = input().split()
d = [int(x) for x in d]

freq = [[] for _ in range(n)]

for idx, x in enumerate(d):
    freq[x].append(idx + 1)

if len(freq[0]) != 1:
    print('-1')
    import sys; return

solution = []
for i in range(1, n):
    if i - 1 != 0:
        new_k = k - 1
    else:
        new_k = k
    if len(freq[i]) > len(freq[i - 1]) * new_k:
        print('-1')
        import sys; return
    prev = freq[i - 1]
    idx = 0
    counter = 0
    for x in freq[i]:
        solution.append((prev[idx], x))
        counter += 1
        if counter == (k if i - 1 == 0 else k - 1):
            idx += 1
            counter = 0

print(len(solution))
for x, y in solution:
    print(x, y)
