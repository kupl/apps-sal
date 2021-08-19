#n = int(input())
#n, m = map(int, input().split())
#d = list(map(int, input().split()))

n = int(input())
d = sorted(map(int, input().split()))

r = 0
j = 1
for i in range(n):
    if j <= d[i]:
        r += 1
        j += 1
print(r)
