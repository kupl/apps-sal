n = int(input())
out = []
cur = 1
while n > 0:
    if n % 2 == 1:
        out.append(cur)
    cur += 1
    n //= 2
for v in reversed(out):
    print(v, end=' ')
print()

