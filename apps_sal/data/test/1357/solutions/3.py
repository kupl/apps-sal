time=0
house=1
n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

for x in a:
    if x!=house:
        if x>house:
            time+= x-house
        else:
            time+= x + n-house
        house = x

print(time)

