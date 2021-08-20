N = int(input())
array = input()
trash = []
count = 0
for i in range(N):
    trash.append(array[i])
    count += 1
    if count >= 3:
        if trash[-1] == 'x' and trash[-2] == 'o' and (trash[-3] == 'f'):
            del trash[-1]
            del trash[-1]
            del trash[-1]
            count -= 3
print(count)
