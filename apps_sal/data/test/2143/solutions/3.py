f = input()

l = list(map(int, input().split()))

d = {}
ans = 0
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        sum = l[i] + l[j]
        if sum in d:
            d[sum] += 1
            if(d[sum] > ans):
                ans = d[sum]
        else:
            d[sum] = 1
            if(d[sum] > ans):
                ans = d[sum]

print(ans)
