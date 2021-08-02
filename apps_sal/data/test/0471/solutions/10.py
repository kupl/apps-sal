n, a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()
if(len(b) == 1):
    print(0)
elif(len(b) == 2):
    print(min(abs(a - b[0]), abs(a - b[1])))
elif(a < b[0]):
    print(b[-2] - a)
elif(a > b[-1]):
    print(a - b[1])
elif(a == b[0]):
    print(b[-2] - a)
elif(a == b[-1]):
    print(a - b[1])
elif(len(b) == 3):
    if(a < b[1]):
        print(min(a - b[0] - b[0] + b[1], b[1] - a + b[1] - a + a - b[0], b[2] - a))
    elif(a > b[1]):
        print(min(a - b[0], a - b[1] + a - b[1] + b[2] - a, b[2] - a + b[2] - a + a - b[1]))
    else:
        print(min(a - b[0], b[2] - a))
elif(a < b[1]):
    print(min(a - b[0] + a - b[0] + b[-2] - a, b[-2] - a + b[-2] - a + a - b[0], b[-1] - a))
elif(a > b[-2]):
    print(min(a - b[0], b[-1] - a + b[-1] - a + a - b[1], a - b[1] + a - b[1] + b[-1] - a))
else:
    print(min(a - b[1] + a - b[1] + b[-1] - a, b[-1] - a + b[-1] - a + a - b[1], a - b[0] + a - b[0] + b[-2] - a, b[-2] - a + b[-2] - a + a - b[0]))
