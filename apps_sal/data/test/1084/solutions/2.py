# python3
n, m = tuple(map(int, input().split()))

mask = 0
collected = set()

while n:
    n -= 1

    row = 0
    for char in input():
        row = (row << 1) | (char == '#')

    if row & mask:
        if row not in collected:
            print("No")
            break
    else:
        mask ^= row
        collected.add(row)
else:
    print("Yes")
