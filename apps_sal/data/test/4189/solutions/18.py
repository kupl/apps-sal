n = int(input().strip())
p = 0
q = 0
for i in range(n):
    (a, b) = input().strip().split()
    if b == 'soft':
        p += 1
    else:
        q += 1
t = 0
while True:
    t += 1
    black = t * t // 2
    white = (t * t + 1) // 2
    if p <= black and q <= white or (p <= white and q <= black):
        print(t)
        break
