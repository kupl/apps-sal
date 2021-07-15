A,B,K = list(map(int, input().split()))
count_list = []
for i in range(1,A+1):
    if A%i == 0 and B%i == 0:
        count_list.append(i)

print((count_list[-K])) 

