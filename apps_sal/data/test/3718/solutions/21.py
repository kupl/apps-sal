n = int(input())
per = list(map(int, input().split()))
per2 = False
for i in range(n -2):
    if per2:
        break
    for j in range(i+1 , n-1):
        if per2:
            break
        for t in range(j+1, n):
            
            if (max(per[t], per[j]) - min(per[t], per[j])) in (1,2) and (max(per[t], per[i]) - min(per[t], per[i])) in (1,2) and (max(per[i] , per[j]) - min(per[i] , per[j])) in (1,2):
                print('YES')
                per2 = True
                break
if not per2:
    print('NO')
