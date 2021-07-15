n, k = list(map(int, input().split()))
a = [1] * n
for i in range(k):
    d = int(input())
    tmp = list(map(int, input().split()))
    for j in tmp:
        a[j - 1] = 0
print((sum(a)))

