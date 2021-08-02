n = int(input())
t = list(map(int, input().split()))
m = int(input())
dr = [None] * m
time = sum(t)
for i in range(m):
    p, x = list(map(int, input().split()))
    p -= 1
    ans = time - t[p] + x
    print(ans)
