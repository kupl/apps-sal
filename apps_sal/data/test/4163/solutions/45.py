N = int(input())
index = 0
for n in range(N):
    Input = input().split()
    if Input[0] == Input[1]:
        index += 1
    else:
        index = 0
    if index == 3:
        break
if index == 3:
    print('Yes')
else:
    print('No')
