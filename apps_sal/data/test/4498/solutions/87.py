a,b,c,d=map(int,input().split(" "))
print(["No","Yes"][(abs(a-b)<=d and abs(c-b)<=d) or abs(a-c)<=d])
