n = int(input())
x, y = map(int, input().split())

def d(a, b):
    return a + b

if d(x-1, y-1) <= d(n-x, n-y):
    print("White")
else:
    print("Black")
