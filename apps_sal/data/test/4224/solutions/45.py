n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(len(a)):
    counter = 0
    while 1:
        if a[i] % 2 == 0:
            counter += 1
            a[i] = a[i] // 2
        else:
            break
    count += counter
print(count)
