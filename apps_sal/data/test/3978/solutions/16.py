n = int(input())
a = [int(x) for x in input().split()]
ans = 0
while(min(a) < 1001):
    ans += 1
    r = min(a)
    for i in range(len(a)):
        if a[i] != 1001:
            if a[i] % r == 0:
                a[i] = 1001
print(ans)
