n = int(input())
s = list(map(int, input().split()))
sm = sum(s)
mx = max(s)
for i in range(mx, 1000000):
    if i * n - sm > sm:
        print(i)
        break
