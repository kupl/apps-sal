f = list(map(int, input().split(':')))
s = list(map(int, input().split(':')))

a = f[0]*60 + f[1]
b = s[0]*60 + s[1]

n = (a+b)//2

print('%02d:%02d' %(n//60, n%60)) 


