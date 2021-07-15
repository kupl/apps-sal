n, x, y = map(int, input().split())

x -= 1
y -= 1

dist = [0] * n
for i in range(0, n):
    for j in range(i+1, n):
        d = min(abs(j-i), abs(x-i)+1+abs(j-y), abs(y-i)+1+abs(j-x))
        dist[d] += 1

for k in range(1, n):
    print(dist[k])
