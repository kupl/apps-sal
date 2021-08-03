n = int(input())
col = list(map(int, input().split()))
low = min(col)
start = int()
store = list()
dist = list()
for i in range(len(col)):
    if col[i] == low:
        store.append(i + 1)
        if i + 1 in range(len(col)):
            start = col[i + 1]
        else:
            start = col[0]

for j in range(len(store)):
    if j == (len(store) - 1):
        dist.append(n - store[-1] + store[0])
    else:
        dist.append(store[j + 1] - store[j])

high = max(dist)

if max(col) == min(col):
    print(max(col) * n)
elif len(store) == 1:
    print(n * (low + 1) - 1)
else:
    print(n * (low) + (high - 1))
