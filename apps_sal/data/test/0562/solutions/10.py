n = int(input())
show = [list(map(int, input().split())) for _ in range(n)]
show.sort(key=lambda x: x[0])
tv1 = tv2 = -1
ans = True
for i in range(n):
    if show[i][0] > tv1:
        tv1 = show[i][1]
    elif show[i][0] > tv2:
        tv2 = show[i][1]
    else:
        ans = False
        break
print('YES' if ans else 'NO')
