import sys

arr = [list( map( int, next(sys.stdin).split() )) for i in range(3)]

def add(a, b):
    return [a[i]+b[i] for i in range(2)]
def sub(a, b):
    return [a[i]-b[i] for i in range(2)]

def div(a, b):
    return [a[i]/b for i in range(2)]

a = add(arr[0], sub(arr[1], arr[2]))
b = add(arr[2], sub(arr[1], arr[0]))
c = add(arr[0], sub(arr[2], arr[1]))

print(3)
print("%d %d"%tuple(a))
print("%d %d"%tuple(b))
print("%d %d"%tuple(c))

