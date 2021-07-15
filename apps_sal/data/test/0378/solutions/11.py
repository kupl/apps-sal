k, r = map(int, input().split())
num = k
counter = 1
while num % 10 not in [r, 0]:
    num += k
    counter += 1
print(counter)
