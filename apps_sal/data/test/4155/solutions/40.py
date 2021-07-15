# Nがちいさいので愚直にやってもいいね
n = int(input())
h = list(map(int, input().split()))
s = sum(h)
count = 0
while s > 0:
    for i in range(n):
        if h[i] == 0:
            continue
        for j in range(i, n):
            if h[j] == 0:
                break
            h[j] -= 1
            s -= 1
        count += 1
        break
print(count)
