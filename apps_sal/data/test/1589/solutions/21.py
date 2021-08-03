n, m = list(map(int, input().split()))
sum = 0
for k in range(n):
    tmp = list(map(int, input().split()))
    i = 0
    for j in range(m):
        if tmp[i] or tmp[i + 1]:
            sum += 1
        i += 2
print(sum)
