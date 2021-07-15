s = [input(), input()]
n = int(input())
ans = [[0] * 101 for i in range(2)]

for i in range(n):
    a = input().split()
    q = 0
    p = 0
    
    if a[3] == 'y': q = 1
    else: q = 2

    if a[1] == 'h': p = 0
    else: p = 1

    if ans[p][int(a[2])] >= 2: continue

    ans[p][int(a[2])] += q

    if ans[p][int(a[2])] >= 2:
        print(s[p] + ' ' + a[2] + ' ' + a[0])


    
        

        

