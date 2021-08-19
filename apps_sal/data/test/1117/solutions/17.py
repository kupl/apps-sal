n = int(input())
ph = 1000000010
valid = 'YES'
for i in range(n):
    (a, b) = [int(x) for x in input().split()]
    if max(a, b) <= ph:
        ph = max(a, b)
    elif min(a, b) <= ph:
        ph = min(a, b)
    else:
        valid = 'NO'
        break
print(valid)
