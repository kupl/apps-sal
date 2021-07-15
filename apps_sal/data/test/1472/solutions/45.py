n, x, y = map(int, input().split())

l = [0] * (n-1)
for i in range(1, n):
    for j in range(i+1, n+1):
        s = min(j-i, abs(x-i)+abs(j-y)+1)
        l[s-1] += 1
for i in l:
    print(i)
