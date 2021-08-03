import math

N, A, B = list(map(int, input().split()))
v = list(map(int, input().split()))

v.sort(reverse=True)
total = 0


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


for i in range(A):
    total = total + v[i]
else:
    print((total / A))

count = 0
min = v[A - 1]
number = v.count(min)

if(v.index(min) == 0):
    for i in range(A, number + 1):
        if(i > B):
            break
        count = combinations_count(number, i) + count
    print(count)
else:
    print((combinations_count(number, A - v.index(min))))
