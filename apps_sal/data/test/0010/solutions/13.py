n = int(input())

s = 2 * (n // 7)
p = s
if(n % 7 > 2):
    s += 2
else:
    s += n % 7
if(n % 7 > 5):
    p += 7 - n % 7
print(p, s)
