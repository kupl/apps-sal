k=input()
n=int(k, base = 2)

pw = 0
s = 0
r = 1
while r < n:
    s += 1
    r *= 4
print(s)
