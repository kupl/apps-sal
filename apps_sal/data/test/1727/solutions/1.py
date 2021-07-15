n = int(input())
k = []
for i in range(n):
    k.append(list(map(int, input().split())))

if n == 1:
    print(1)
else:
    ans = 2
    for i in range(1, n-1):
        if k[i][0]-k[i][1] > k[i-1][0]:
            ans += 1
        elif k[i][0]+k[i][1] < k[i+1][0]:
            k[i][0] += k[i][1]
            ans += 1
    print(ans)
