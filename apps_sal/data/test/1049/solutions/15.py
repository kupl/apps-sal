n, d = [int(x) for x in input().split()]
max_vic = 0
vic = 0
test = '1'*n
for i in range(d):
    if input() == test:
        max_vic = max(vic, max_vic)
        vic = 0
    else:
        vic += 1
max_vic = max(vic, max_vic)
print(max_vic)



