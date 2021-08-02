# July 4, 2013
def luck(n):
    total = 0
    for char in n:
        if char == '4' or char == '7':
            total += 1
    return total


sa = input().split(' ')
magic = int(sa[1])
check = input().split(' ')
total1 = 0
for element in check:
    if luck(element) <= magic:
        total1 += 1
print(total1)
