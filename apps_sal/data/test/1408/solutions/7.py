one = []
two = []

x=int(input())
for i in range(x):
    a, b = list(map(int, input().split(' ')))
    if a == 1:
        one.append(b)
    else:
        two.append(b)

one.sort()
two.sort()
minx = 9000000

for ones in range(0, len(one)+1):
    for twos in range(0,len(two)+1):
        w = ones + 2 * twos
        a = sum(one[:len(one)-ones]) + sum(two[:len(two)-twos])
        if a <= w: 
            minx = min(minx, w)
print(minx)
