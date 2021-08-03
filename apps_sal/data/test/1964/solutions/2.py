n = int(input())
k = list(map(int, input().split()))
now = 0
m = 100000000
for i in range(n):
    b = map(int, input().split())
    now = 0
    for j in b:
        now += j * 5 + 15
    m = min(m, now)
print(m)
