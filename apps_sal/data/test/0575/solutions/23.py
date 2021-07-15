n = int(input())
f1 , f2 = map(int, input().split())
k1 , k2 = map(int, input().split())
k21 , k22 = map(int, input().split())
if ((k1 < f1 and k21 < f1 and k2 < f2 and k22 < f2) or (k1 > f1 and k21 > f1 and k2 < f2 and k22 < f2) or (k1 < f1 and k21 < f1 and k2 > f2 and k22 > f2) or (k1 > f1 and k21 > f1 and k2 > f2 and k22 > f2)):
    print('YES')
else:
    print('NO')
