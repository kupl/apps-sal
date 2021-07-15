m,d= list(map(int,input().split()))
c = [0,31,28,31,30,31,30,31,31,30,31,30,31]
num = d - 1 + c[m]
col = num // 7;
if num % 7 != 0:
    col+=1
print(col)

