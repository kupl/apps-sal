A, B = map(int, input().split())

a = 0
num = 1
while num < B:
    num -= 1
    num += A
    a += 1

print(a)
