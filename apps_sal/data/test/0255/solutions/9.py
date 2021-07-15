n = int(input())
na = sorted(list(map(int, input().split())))

m = int(input())
ma = sorted(list(map(int, input().split())))
ans = 0

for i in range(n):
    for j in range(m):
        if abs(ma[j] - na[i]) <= 1:
            ans += 1
            ma[j] = -100
            na[i] = -100500

print(ans)




