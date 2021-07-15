n, t, c = [int(x) for x in input().split()]
prisoners = [int(x) for x in input().split()]

total = 0
current = 0

for i in prisoners:
    if i > t:
        if (current >= c):
            total += current - c + 1            
        current = 0
    else:
        current += 1

if (current >= c):
    total += current - c + 1

print(total)
            
            

