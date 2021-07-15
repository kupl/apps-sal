ooo = input()
m = [int(i) for i in input().split()]
k = False
for i in range(int(ooo)-1):
    if abs(m[i]-m[i+1]) > 1:
        print('NO')
        k = True
        break
if not k:print('YES')
