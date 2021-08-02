n, c = list(map(int, input().split()))
w = list(map(int, input().split()))
r = 1
for i in range(1, n):
    if w[i] - w[i - 1] > c:
        r = 1
    else:
        r += 1
print(r)
