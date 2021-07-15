X = int(input())

maxi = 0

if X < 4:
    print(1)
    return

for i in range(1, X+1):
    for j in range(2, X+1):
        if i**j <= X and i**j >= maxi:
            maxi = i**j
        if i**j > X:
            break

print(maxi)
