n, m = map(int, input().split())

mat = []
maxi = 0
for i in range(n):
    a = list(map(int, input().split()))
    mini = min(a)
    maxi = max(maxi, mini)
print(maxi)
