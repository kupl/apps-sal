maxst = 0
count = 0
n = int(input())
M = input().split()
for i in range(0, n):
    ni = int(M[i])
    for j in range(maxst, 30):
        if ni % 2 ** j == 0:
            if maxst < j:
                maxst = j
                count = 0
            count += 1
        else:
            break
print(2 ** maxst, count)
