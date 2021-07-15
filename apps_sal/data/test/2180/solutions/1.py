n = int(input())

print((n*n+1)//2)
on = "C."*(n//2)+("C" if n%2 else "")
off = ".C"*(n//2)+("." if n%2 else "")
for i in range(n):
    if i % 2: print(off)
    else: print(on)

