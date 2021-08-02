N = int(input())

p = []

for i in range(N):
    p.append(int(input()))

p.sort()
p.reverse()

p[0] //= 2

print(sum(p))
