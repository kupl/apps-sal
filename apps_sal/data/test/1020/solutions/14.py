w = input().split(' ')

n = int(w[0])
m = int(w[1])
k = int(w[2])

sm = 0

while k > 0:
    sm += 2 * (n + m - 2)
    n -= 4
    m -= 4
    k -= 1

print(sm)
