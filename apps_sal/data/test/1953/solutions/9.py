n = int(input())
ns = sorted(map(int, str.split(input())))
happy = time = 0
for n in ns:

    if time <= n:

        time += n
        happy += 1

print(happy)

