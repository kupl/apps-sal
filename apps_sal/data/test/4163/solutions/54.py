
N = int(input())

D = []

for i in range(N):
    D1,D2 = input().split()
    D.append([D1,D2])

for i in range(N-2):
    for j in range(3):
        if D[j+i][0] != D[j+i][1]:
            break
    
    else:
        print('Yes')
        return

print('No')

