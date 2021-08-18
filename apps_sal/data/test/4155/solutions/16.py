n = int(input())
h = list(map(int, input().split()))
s = sum(h)
count = 0
while s > 0:
    f = False
    for i in range(n):
        if f:
            break
        if h[i] == 0:
            continue
        for j in range(i, n):
            if h[j] == 0:
                f = True
                break
            h[j] -= 1
            s -= 1
        count += 1
        break
print(count)
