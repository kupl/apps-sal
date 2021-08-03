a, m = list(map(int, str.split(input())))
mem = set()
while a not in mem:

    mem.add(a)
    if a % m == 0:

        print("Yes")
        return

    else:

        a = (a + a % m) % m

print("No")
