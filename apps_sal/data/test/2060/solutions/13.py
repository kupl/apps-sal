n = int(input())
a = []
for i in range(101):
    for j in range(101):
        a.insert(0, i * 3 + j * 7)
for i in range(n):
    x = int(input())
    print('YES' if x in a else 'NO')
