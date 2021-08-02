a = int(input())

while sum(list(map(int, list(str(a))))) % 4 != 0:
    a += 1

print(a)
