N, X = list(map(int, input().split()))
a = [int(input()) for _ in range(N)] 
sum_material = sum(a)
b = min(a)
count = 0
X = X - sum_material
if X < b:
    print((len(a)))
else:
    while X >= b:
        X -= b
        count += 1
    print((len(a) + count))


