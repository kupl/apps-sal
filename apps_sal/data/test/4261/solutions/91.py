(a, b, c) = map(int, input().split())
container1 = a - b
container2 = c - container1
if container2 > 0:
    print(container2)
else:
    print(0)
