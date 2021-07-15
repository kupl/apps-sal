n = int(input())
a = list(map(int,input().split()))
b = set(a)
for i in range(n-1,-1,-1):
    b.discard(a[i])
    if not b:
        print(a[i])
        break

