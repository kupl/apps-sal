N = int(input())
N_List = list(map(int, input().split()))
NR_List = [i // 400 for i in N_List]
Number_NRD = len(set([i for i in NR_List if i < 8]))
Number_NRU = len([i for i in NR_List if i >= 8])
max_p = Number_NRD + Number_NRU
min_p = (Number_NRD, 1)[Number_NRD == 0]
print(str(min_p) + ' ' + str(max_p))
