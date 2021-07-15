def low_bound(mas, x):
    l = 0
    r = len(mas) - 1
    while l < r:
        m = (l + r) // 2
        if mas[m][0] >= x:
            r = m
        else:
            l = m + 1
    return l

n = int(input().strip())
gr = []
for i in range(n):
    gr.append(list(map(int, input().split()))[::-1] + [i + 1])
k = int(input().strip())
tab = [[v, i + 1] for i, v in enumerate(list(map(int, input().split())))]
gr.sort(reverse = True)
ans = []
s = 0
tab.sort()
for p, cnt, ind in gr:
    if len(tab) > 0 and tab[-1][0] >= cnt:
        s += p
        i = low_bound(tab, cnt)
        ans.append((ind, tab[i][1], ))
        tab.remove(tab[i])
    
print(len(ans), s)
for i in ans:
    print(*i)
        
tab.sort()

