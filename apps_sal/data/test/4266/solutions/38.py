(k, x) = map(int, input().split())
arr = []
for i in range(x - k + 1, x + k):
    arr.append(str(i))
print(' '.join(arr))
