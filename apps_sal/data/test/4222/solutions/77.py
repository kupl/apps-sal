(n, k) = map(int, input().split())
l = [0] * n
for i in range(k):
    d = int(input())
    x = list(map(int, input().split()))
    for j in range(d):
        l[x[j] - 1] += 1
print(l.count(0))
