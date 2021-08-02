n, k = map(int, input().split())

sum: float = 0.0
for i in range(1, n + 1):
    ret: float = 1 / n
    tmp = i
    while(tmp < k):
        tmp *= 2
        ret /= 2
    if(tmp != 0):
        sum += ret
print(sum)
