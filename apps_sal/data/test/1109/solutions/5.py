n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
ans = 0
for i in range(k):
    ones = 0
    twos = 0
    for j in range(n // k):
        num = l[i + j * k]
        if(num == 1):
            ones += 1
        else:
            twos += 1
    ans += min(ones, twos)
print(ans)
