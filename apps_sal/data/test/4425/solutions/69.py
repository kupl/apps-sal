n, k = list(map(int, input().split()))

ans = 0

for i in range(1, n+1):
    count = 0
    p = i
    while p<k:
        p = p*2
        count +=1
    ans += (1/n)*((1/2)**count)

print(ans)
