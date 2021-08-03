n, m = [int(i) for i in input().split()]
a = input().split()
result = []
prev = [-1] * n
for i in range(1, n):
    if a[i] != a[i - 1]:
        prev[i] = i - 1
    else:
        prev[i] = prev[i - 1]
for i in range(m):
    l, r, x = input().split()
    r = int(r)
    if a[r - 1] != x:
        answer = r
    elif prev[r - 1] < int(l) - 1:
        answer = -1
    else:
        answer = prev[r - 1] + 1
    result.append(str(answer))
print('\n' .join(result))
