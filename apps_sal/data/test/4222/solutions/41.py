n, k = list(map(int, input().split()))

sunuke = [0] * n

for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    if d <= 1:
        sunuke[a[0] - 1] += 1
    else:
        for i in range(d):
            sunuke[a[i] - 1] += 1

# print(sunuke)
print((sunuke.count(0)))
