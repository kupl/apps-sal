a,b,c,d=map(int, input().split())
print("Yes" if abs(c-a)<=d or (abs(a-b)<=d and abs(b-c)<=d)  else "No")
