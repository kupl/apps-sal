from datetime import date
a = date(*list(map(int,input().split(':'))))
b = date(*list(map(int,input().split(':'))))
print(abs(a-b).days) 

