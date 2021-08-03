n, a, b = [int(x) for x in input().split()]
ports = [int(x) for x in input()]
if ports[a - 1] == ports[b - 1]:
    print(0)
else:
    print(1)
