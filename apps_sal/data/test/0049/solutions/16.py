k = int(input())
x = 0
c = 0
while(x < k):
    x += 9 * (10**c) * (c + 1)
    c += 1
p = (x - k) % c
k = ((10**c) - int(((x - k) / c)) - 1)
k = str(k)
print(k[len(k) - (p) - 1])
