N_list = []
for i in range(3):
    N = input()
    N_i = N[0:3]
    N_list.append(N_i)
    i += 1
print(N_list[0][0] + N_list[1][1] + N_list[2][2])
