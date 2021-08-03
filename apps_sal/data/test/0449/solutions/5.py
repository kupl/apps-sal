n = int(input())
r = 0
l = [1, 5, 10, 20, 100]
while n > 0:
    i = len(l) - 1
    while l[i] > n:
        i -= 1
    n -= l[i]
    r += 1
print(r)
