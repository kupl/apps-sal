def isequal(a, b):
    return abs(a-b) <= 0.00000001
a, b, c = list(map(int, input().split(' ')))
slopes = []
for i in range(a):
    x, y = list(map(int, input().split(' ')))
    if x == b:
        slopes.append(90001)
    else:
        slopes.append((y-c)/(x-b))
print(len(set(slopes)))

