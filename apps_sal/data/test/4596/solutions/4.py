n = int(input())
a = list(map(int, input().split()))
count = 0

while True:
    odd = False
    for x in range(n):
        if a[x] % 2 != 0:
            odd = True
            break
        else:
            a[x] //= 2
    if odd:
        break
    count += 1

print(count)
