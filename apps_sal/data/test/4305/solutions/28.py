h,a = map(int,input().split())
print([h//a+1,h//a][h%a==0])
