# map(int, input().split())
# list(map(int, input().split()))

n, m = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()

pos = [(b[i] - a[0]) % m for i in range(n)]

for x in pos:
    new = [(a[i] + x) % m for i in range(n)]
    new.sort()
    if (new == b):
        print(x)
        break
