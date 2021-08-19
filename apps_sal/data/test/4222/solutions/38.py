(n, k) = map(int, input().split())
trick = [0] * n
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for i in range(d):
        trick[a[i] - 1] = 1
print(trick.count(0))
