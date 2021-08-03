
n, m = list(map(int, input().split()))

print(min(n, m) + 1)

for i in range(min(n, m) + 1):
    if(m > n):
        print(i, m - i)
    else:
        print(n - i, i)
