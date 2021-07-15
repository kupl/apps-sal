a,b,x = map(int, input().split())

a_div=0
b_div = b//x
if a!=0:
    a_div = (a-1)//x
    count = b_div-a_div
else:
    count = b_div-a_div+1
print(count)
