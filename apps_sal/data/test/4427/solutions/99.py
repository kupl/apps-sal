details = list(map(int, input().split()))
r = details[0]
D = details[1]
x = details[2]
current = x
for i in range(10):
    thing = r * current - D
    print(thing)
    current = thing
