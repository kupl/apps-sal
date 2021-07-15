game = list(map(int, input().split()))
seq = list(map(int, list(input())))

c = 0

for i in seq:
    c+=game[i-1]
print(c)

