n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in range(n - 1, -1, -1):
    if k % a[i] == 0:
        print(k // a[i])
        break
