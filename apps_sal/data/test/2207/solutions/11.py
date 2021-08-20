inc = input().split(' ')
for i in range(int(inc[0])):
    foundation = input()
bl = True
block = 0
for i in range(int(inc[1])):
    if bl and foundation[i] == 'B':
        bl = False
        block += 1
    elif not bl and foundation[i] == '.':
        bl = True
print(block)
