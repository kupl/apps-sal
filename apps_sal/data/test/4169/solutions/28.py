#a値段,b本数
#n軒,m本
n,m = list(map(int, input().split()))

ab_list = [list(map(int, input().split())) for _ in range(n)]
#print(ab_list)
ab_list.sort()
ans = 0
num = 0
for ab in ab_list:
    ans += ab[0]*ab[1]
    num += ab[1]
    if num >= m:
        i_stop=ab_list.index(ab)
        break
diff_num = num - m
ans -= diff_num * ab_list[i_stop][0]
print(ans)
