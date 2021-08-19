(n, k) = list(map(int, input().split()))
sunukes = [0 for i in range(n)]
for i in range(k):
    d = int(input())
    aa = list(map(int, input().split()))
    for j in range(d):
        sunukes[aa[j] - 1] += 1
count = sum((1 for sunuke in sunukes if sunuke == 0))
print(count)
