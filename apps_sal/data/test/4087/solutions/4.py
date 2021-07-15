a = int(input())
while sum(list(map(int, str(a)))) % 4:
    a += 1
print(a)
