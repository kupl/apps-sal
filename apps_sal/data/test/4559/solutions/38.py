input()
a = 1
for i in input().split():
    a *= int(i)
    a = [-1, a][0 <= a <= 10 ** 18]
print(a)
