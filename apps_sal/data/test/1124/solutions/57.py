def GCD(a, b):
    if (b == 0):
        return a;
    else:
        return GCD(b, a % b);


n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    cnt = GCD(cnt, a[i])
print(cnt)
