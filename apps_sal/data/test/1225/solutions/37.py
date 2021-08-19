H = int(input())
count = 0
pow = 1
for _ in range(H):
    if H < pow:
        break
    count += 1
    pow *= 2
print(2 ** count - 1)
