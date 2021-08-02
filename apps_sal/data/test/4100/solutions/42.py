n, k, q = map(int, input().split())
a = [0 for i in range(n)]
for i in range(q):
    x = int(input())
    a[x - 1] += 1
for i in range(n):
    print("Yes" if a[i] - (q - k) > 0 else "No")
