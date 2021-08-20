s = input().split(' ')
k = int(s[0])
r = int(s[1])
count = 1
while True:
    if k * count % 10 == 0 or k * count % 10 == r:
        break
    count += 1
print(count)
