stones = input()
moves = input()

index = 0
for i in moves:
    if i == stones[index]:
        index += 1
print(index + 1)
