n = int(input())
while True:
    if sum([int(k) for k in str(n)]) % 4 == 0:
        break
    n += 1
print(n)
