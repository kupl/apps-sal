n = int(input())
m = [1]
k = 2
while m[-1] < n:
    m.append((2**k - 1) * (2**(k - 1)))
    k += 1
for x in reversed(m):
    if n % x == 0:
        print(x)
        break
