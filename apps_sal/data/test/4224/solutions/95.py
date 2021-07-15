n = int(input())
a = list(map(int, input().split()))
num = 0
for i in a:
    if i%2 == 0:
        t = i
        z = 'YES'
        while z == 'YES':
            if t%2 == 0:
                num += 1
                t /= 2
            else:
                z == 'NO'
                break
print(num)
