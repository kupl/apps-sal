n,m = map(int, input().split())
print(min(n, m)+1)
for i in range(0,min(n,m)+1):
    print(i, abs(min(n,m)-i))
