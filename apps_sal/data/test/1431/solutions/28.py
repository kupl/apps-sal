N = int(input())
a = list(map(int, input().split()))
b = [0] * (N + 1)
for i in range(N, 0, -1):
    if sum(b[::i]) % 2 != a[i - 1]:
        b[i] = 1
s = sum(b)
print(sum(b))
if s != 0:
    for i in range(N + 1):
        if b[i] == 1:
            print(i, end=' ')
