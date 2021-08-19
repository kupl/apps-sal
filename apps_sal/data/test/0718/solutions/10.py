cur = int(input()) + 1
steps = 1
while not '8' in str(cur):
    cur += 1
    steps += 1
print(steps)
