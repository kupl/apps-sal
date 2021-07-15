data = input().split()

N, M = int(data[0]), int(data[1])

table = []
for i in range(N):
    table.append(input().split())

answer = 0

## for first row
if any(e == '1' for e in table[0]):
    answer = 2
##  for last row
elif any(e == '1' for e in table[-1]):
    answer = 2
## for first and  last column
else:
    for i in range(N):
        if table[i][0] == '1':
            answer = 2
        elif table[i][-1] == '1':
            answer = 2

if answer == 0:
    print('4')
else:
    print(answer)
        

