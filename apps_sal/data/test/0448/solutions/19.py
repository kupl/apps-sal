n, m = map(int, input().split())
arr = list(map(int, input().split()))
ids = [i for i in range(1, n + 1)]
while len(ids) > 1:
    index = ids[0]
    del ids[0]
    if arr[index - 1] - m > 0:
        arr[index - 1] -= m
        ids.append(index)
print(ids[0])
