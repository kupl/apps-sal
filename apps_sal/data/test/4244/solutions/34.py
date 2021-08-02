ans = 1000000
n = int(input())
X = list(map(int, input().split()))
for i in range(1, 101):
    tmp = 0
    for x in X:
        tmp += (x - i)**2
    ans = min(ans, tmp)
print(ans)
