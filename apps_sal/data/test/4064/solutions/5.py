
n, h, l, r = list(map(int, input().split()))
N = n

a = list(map(int, input().split()))

flag = True
i = -1
lis = [float("-inf")] * h
lis[0] = 0
ans = 0

for i in range(N):

    nlis = [float("-inf")] * h

    na = a[i]
    for j in range(h):

        if l <= (j + na) % h <= r:
            nlis[(j + na) % h] = max(nlis[(j + na) % h], lis[j] + 1)
        else:
            nlis[(j + na) % h] = max(nlis[(j + na) % h], lis[j])

        if l <= (j + na - 1) % h <= r:
            nlis[(j + na - 1) % h] = max(nlis[(j + na - 1) % h], lis[j] + 1)
        else:
            nlis[(j + na - 1) % h] = max(nlis[(j + na - 1) % h], lis[j])

    lis = nlis

print(max(0, max(lis)))
