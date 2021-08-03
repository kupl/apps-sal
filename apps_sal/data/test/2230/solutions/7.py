n = input()
n = int(n)
bags = []
for i in range(n**2):
    bags.append(i + 1)

start = 0
end = -1
step = int(n / 2)

for i in range(n):
    for j in range(start, start + step):
        print(bags[j], end=' ')
    start += step
    for j in range(end, end - step, -1):
        print(bags[j], end=' ')
    end -= step
    print('')
