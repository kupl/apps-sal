N, D = map(int,input().split())
n_list = []

for i in range(1,N+1):
    n_list.append(i)
num = len(n_list) % ((2 * D) + 1)
if num == 0:
    print(len(n_list) // ((2 * D) + 1))
else:
    print((len(n_list) // ((2 * D) + 1))+1)
