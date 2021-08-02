n = int(input())
tl = list(map(int, input().split()))
time = sum(tl)
m = int(input())

for _ in range(m):
    p, x = list(map(int, input().split()))
    print((time - (tl[p - 1] - x)))
