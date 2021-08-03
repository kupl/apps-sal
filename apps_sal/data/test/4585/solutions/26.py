x = int(input())

t = 0
while True:
    if not (t * (t + 1)) / 2 >= x:
        t += 1
    else:
        break
print(t)
