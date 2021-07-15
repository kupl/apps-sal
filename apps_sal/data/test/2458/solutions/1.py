t, k = list(map(int, input().split(' ')))
values = [0] + [1] + [0] * (10**5+10)
sums = [0] + [1] + [0] * (10**5+10)
for i in range(2, 10**5+10):
    values[i] = (values[i-1] + values[max(0, i-k)])%(10**9+7)
    sums[i] = (sums[i-1] + values[i])%(10**9+7)
    
for i in range(t):
    a, b = list(map(int, input().split(' ')))
    print((sums[b+1]-sums[a])%(10**9+7))

