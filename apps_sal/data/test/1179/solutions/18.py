n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
i = 1
while k > i:
    k -= i
    i += 1
print(a[k - 1])
