N = int(input())
N_list = []
for i in range(1,N+1):
    if len(str(i)) % 2 == 1:
        N_list.append(i)
print(len(N_list))
