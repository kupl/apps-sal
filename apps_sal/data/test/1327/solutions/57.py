n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

sum_list = [0] * 8

l_ppp = [0] * n
l_ppm = [0] * n
l_pmp = [0] * n
l_mpp = [0] * n
l_pmm = [0] * n
l_mpm = [0] * n
l_mmp = [0] * n
l_mmm = [0] * n

for i in range(n):
    l_ppp[i] = l[i][0] + l[i][1] + l[i][2]
    l_ppm[i] = l[i][0] + l[i][1] - l[i][2]
    l_pmp[i] = l[i][0] - l[i][1] + l[i][2]
    l_mpp[i] = - l[i][0] + l[i][1] + l[i][2]
    l_pmm[i] = l[i][0] - l[i][1] - l[i][2]
    l_mpm[i] = - l[i][0] + l[i][1] - l[i][2]
    l_mmp[i] = - l[i][0] - l[i][1] + l[i][2]
    l_mmm[i] = - l[i][0] - l[i][1] - l[i][2]

l_ppp = sorted(l_ppp, reverse=True)
l_ppm = sorted(l_ppm, reverse=True)
l_pmp = sorted(l_pmp, reverse=True)
l_mpp = sorted(l_mpp, reverse=True)
l_pmm = sorted(l_pmm, reverse=True)
l_mpm = sorted(l_mpm, reverse=True)
l_mmp = sorted(l_mmp, reverse=True)
l_mmm = sorted(l_mmm, reverse=True)

sum_list[0] = sum(l_ppp[:m])
sum_list[1] = sum(l_ppm[:m])
sum_list[2] = sum(l_pmp[:m])
sum_list[3] = sum(l_mpp[:m])
sum_list[4] = sum(l_pmm[:m])
sum_list[5] = sum(l_mpm[:m])
sum_list[6] = sum(l_mmp[:m])
sum_list[7] = sum(l_mmm[:m])

print(max(sum_list))
