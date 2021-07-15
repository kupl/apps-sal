# -*- coding: utf-8 -*-

N = int(input().strip())
AB_list = [list(map(int, input().rstrip().split())) for i in range(N)]
#-----

A_list,B_list = list(map(list, list(zip(*AB_list))))

A_list.sort()
B_list.sort()


if N%2 == 0:
    Med_A = A_list[ (N-1)//2 ] + A_list[ (N-1)//2 + 1 ]
    Med_B = B_list[ (N-1)//2 ] + B_list[ (N-1)//2 + 1 ]
    
else:
    Med_A = A_list[ (N-1)//2 ]
    Med_B = B_list[ (N-1)//2 ]


Med_range = Med_B - Med_A + 1
print(Med_range)

