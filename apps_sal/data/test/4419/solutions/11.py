# map(int, input().split())
rw = int(input())
for wewq in range(rw):
    a, b = list(map(int, input().split()))
    d = abs(a - b)
    print((d + 9) // 10)
