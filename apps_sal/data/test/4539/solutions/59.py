n = int(input())
m = list(str(n))
f = sum([int(m) for m in m ])

print("Yes") if n%f==0 else print("No")
