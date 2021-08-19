inputs = input().split(' ')
N = int(inputs[0])
X = int(inputs[1])
T = int(inputs[2])
remaining = N
time = 0
while remaining > 0:
    remaining -= X
    time += T
print(time)
