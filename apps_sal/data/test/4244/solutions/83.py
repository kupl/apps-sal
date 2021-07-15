N = int(input())
X = list(map(int, input().split()))
ans = 10**18

for p in range(1, 101):
    tmp = 0
    for x in X:
        tmp += (x-p)**2
    ans = min(tmp, ans)

print(ans)



