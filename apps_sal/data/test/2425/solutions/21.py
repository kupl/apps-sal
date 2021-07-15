def intlog2(n):
    if n <= 0:
        return -1
    i = 0
    while 2**i <= n:
        i += 1
    return i-1

def isfull(n):
    a = intlog2(n)
    if n == (1<<a+1) - 1:
        return 1
    else:
        return 0

def calc(n):
    a  = intlog2(n)
    if isfull(n):
        return [1, 1, 5, 1, 21, 1, 85, 73, 341, 89, 1365, 1, 5461, 4681, 21845, 1, 87381, 1, 349525, 299593, 1398101, 178481, 5592405, 1082401][a-1]
    else:
        return (1<<a+1)-1

q = int(input())
for _ in range(q):
    a = int(input())
    print(calc(a))

