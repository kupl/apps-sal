t = int(input())
for i in range(t):
    n = int(input())
    a = [int(j) for j in input().split()]
    used = set()
    for j in a:
        if j % 2 == 1:
            continue
        while j % 2 == 0 and j not in used:
            used.add(j)
            j /= 2
    print(len(used))
