N = int(input())
h = list(map(int, input().split()))
h.append(0)

t = 0

def Water(n):
    nonlocal h
    while h[n] != 0:
        h[n] -= 1
        n += 1
        #print(h, t)

for i in range(N):
    while h[i] != 0:
        Water(i)
        t += 1

print(t)
