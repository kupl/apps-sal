(a, b) = list(map(int, input().split()))
count = 0
while True:
    (a, b) = (min(a, b), max(a, b))
    while b > 2:
        a += 1
        b -= 2
        count += 1
    if b == 2 and a <= 2 or (a == 2 and b <= 2):
        count += 1
        break
    if b == 1 and a == 1:
        break
print(count)
