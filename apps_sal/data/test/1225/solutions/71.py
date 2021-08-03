h = int(input())
count = 0
while True:
    h = h // 2
    if h == 0:
        break
    count += 1
print(2**count + int(2**(count) - 1))
