def f1(a,b):
    return abs(a-b)

def f2(a,b):
    a, b = max(a,b), min(a,b)
    b += 10
    return b-a

n = int(input())
a = [int(x) for x in list(input())]
b = [int(x) for x in list(input())]


print(sum(min(f1(x,y),f2(x,y)) for x,y in zip(a,b)))
