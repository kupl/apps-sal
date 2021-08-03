a = input()
result = ''
p = -1
if len(a) % 2 == 0:
    p = 1
else:
    p = 0
ul = 0
ur = len(a) - 1
while len(result) < len(a):
    if p == 1:
        result += a[ur]
        ur -= 1
        p = 0
    else:
        result += a[ul]
        ul += 1
        p = 1
print(result[::-1])
