n, x, y = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    rain = a[i]
    for j in range(max(0, i - x), min(i + y + 1, n)):
        if j == i:
            continue
        if rain >= a[j]:
            break
    else:
        print(i + 1)
        break
