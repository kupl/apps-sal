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
list_xyz1.sort()
list_xyz2.sort()
list_xyz3.sort()
list_xyz4.sort()
list_xyz5.sort()
list_xyz6.sort()
list_xyz7.sort()
list_xyz8.sort()
xyz1 = 0
xyz2 = 0
xyz3 = 0
xyz4 = 0
xyz5 = 0
xyz6 = 0
xyz7 = 0
xyz8 = 0
for i in range(M):
    xyz1 += list_xyz1[N - i - 1]
    xyz2 += list_xyz2[N - i - 1]
    xyz3 += list_xyz3[N - i - 1]
    xyz4 += list_xyz4[N - i - 1]
    xyz5 += list_xyz5[N - i - 1]
    xyz6 += list_xyz6[N - i - 1]
    xyz7 += list_xyz7[N - i - 1]
    xyz8 += list_xyz8[N - i - 1]
print(max(xyz1, xyz2, xyz3, xyz4, xyz5, xyz6, xyz7, xyz8))
