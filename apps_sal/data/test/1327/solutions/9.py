(N, M) = map(int, input().split())
num_list = []
for i in range(N):
    num_list.append(list(map(int, input().split())))
'\n[x,y,z]としてx+y+z,x-y+z,x+y-z,x-y-z,-x+y+z,-x-y+z,-x+y-z,-x-y-zの8パターン\nを計算してソート\n'
list_xyz1 = []
list_xyz2 = []
list_xyz3 = []
list_xyz4 = []
list_xyz5 = []
list_xyz6 = []
list_xyz7 = []
list_xyz8 = []
for i in range(N):
    list_xyz1.append(num_list[i][0] + num_list[i][1] + num_list[i][2])
    list_xyz2.append(num_list[i][0] - num_list[i][1] + num_list[i][2])
    list_xyz3.append(num_list[i][0] + num_list[i][1] - num_list[i][2])
    list_xyz4.append(num_list[i][0] - num_list[i][1] - num_list[i][2])
    list_xyz5.append(-num_list[i][0] + num_list[i][1] + num_list[i][2])
    list_xyz6.append(-num_list[i][0] - num_list[i][1] + num_list[i][2])
    list_xyz7.append(-num_list[i][0] + num_list[i][1] - num_list[i][2])
    list_xyz8.append(-num_list[i][0] - num_list[i][1] - num_list[i][2])
list_xyz1.sort(reverse=True)
list_xyz2.sort(reverse=True)
list_xyz3.sort(reverse=True)
list_xyz4.sort(reverse=True)
list_xyz5.sort(reverse=True)
list_xyz6.sort(reverse=True)
list_xyz7.sort(reverse=True)
list_xyz8.sort(reverse=True)
xyz1 = 0
xyz2 = 0
xyz3 = 0
xyz4 = 0
xyz5 = 0
xyz6 = 0
xyz7 = 0
xyz8 = 0
for i in range(M):
    xyz1 += list_xyz1[i]
    xyz2 += list_xyz2[i]
    xyz3 += list_xyz3[i]
    xyz4 += list_xyz4[i]
    xyz5 += list_xyz5[i]
    xyz6 += list_xyz6[i]
    xyz7 += list_xyz7[i]
    xyz8 += list_xyz8[i]
print(max(xyz1, xyz2, xyz3, xyz4, xyz5, xyz6, xyz7, xyz8))
