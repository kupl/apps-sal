N = int(input())
p = [int(n) for n in input().split()]

count = 1
val_min = p[0]
for i in range(1, N):
    if val_min >= p[i]:
        count += 1
       
    val_min = min(val_min, p[i])

print(count)
