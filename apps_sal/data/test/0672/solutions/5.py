(a, b) = [int(i) for i in input().split()]
o = a - b
sum = 0
l = 1
if o > 0:
    for i in range(1, int(o ** 0.5) + l):
        if o % i == 0:
            if o // i > b and i > b:
                sum += 2
                if i == o // i:
                    sum -= 1
            if o // i > b and i <= b or (o // i <= b and i > b):
                sum += 1
if o == 0:
    print('infinity')
else:
    print(sum)
