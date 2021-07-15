n = int(input())

A = input().split()

current_max = 1
days = 0

for i in range(1,n+1):

    current_max=max(current_max,int(A[i-1]))
    if i == current_max:
        ##print(i)
        days += 1

print(days)

