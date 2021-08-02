n = int(input())

p_one = input()
p_one_list = p_one.split(' ')

zmax = int(p_one_list[0]) + int(p_one_list[1])
zmin = int(p_one_list[0]) + int(p_one_list[1])
wmax = int(p_one_list[0]) - int(p_one_list[1])
wmin = int(p_one_list[0]) - int(p_one_list[1])


for i in range(1, n):
    line = input()
    tmp = line.split(' ')
    z = int(tmp[0]) + int(tmp[1])
    w = int(tmp[0]) - int(tmp[1])
    zmax = max(zmax, z)
    wmax = max(wmax, w)
    zmin = min(zmin, z)
    wmin = min(wmin, w)


z_ans = zmax - zmin
w_ans = wmax - wmin


print(f'{max(z_ans, w_ans)}')
