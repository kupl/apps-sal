n = int(input())
val = 0
for i in range(n):
    p, q = (int(x) for x in input().split())
    if q - p >= 2:
        val += 1
print(val)
