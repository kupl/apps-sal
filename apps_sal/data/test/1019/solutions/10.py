def NOD(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


n = int(input())
a = 1
b = n - 1
maximal = []
while b > a:
    if NOD(a, b) == 1:
        maximal = [a, b]
    b = b - 1
    a = a + 1
print(maximal[0], maximal[1])
