n, k = map(int, input().split())
a = list(map(int, input().split()))

max_l = 10**9
min_l = 0
while max_l - min_l != 1:
    count = 0
    mean = (max_l+min_l)//2
    for i in range(n):
        count += -(-a[i]//mean)-1
    if count <= k:
        max_l = mean
    else:
        min_l = mean
print(max_l)
