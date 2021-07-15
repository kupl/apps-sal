n = int(input())
a = 111
for _ in range(9):
    if n <= a:
        print(a)
        return
    a += 111
