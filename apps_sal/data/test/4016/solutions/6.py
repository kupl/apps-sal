(n, k) = list(map(int, input().strip().split()))
st = [i for i in input()]
p = n
for i in range(1, n):
    if st[i:] == st[:n - i]:
        p = i
        break
print(''.join(st) + ''.join(st[n - p:]) * (k - 1))
