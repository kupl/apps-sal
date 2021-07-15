s = input()
r,g,b = map(int,s.split())

print(max([i+(r-i)//3+(g-i)//3+(b-i)//3 for i in range(3) if i <= r and i <= g and i <= b]))
