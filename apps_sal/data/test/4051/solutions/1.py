n = int(input())
f = 0
a = list(map(int, input().split()))
for i in range(n - 1):
    if(abs(a[i] - a[i + 1]) > 1):
        f = 1
print(["YES", "NO"][f])
