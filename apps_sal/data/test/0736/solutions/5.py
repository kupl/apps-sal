n, m = map(int, input().split())
for i in range(n//2+n%2, n+1):
    if i % m == 0:
        print(i)
        break
else:
    print(-1)
