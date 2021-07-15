N = input()
n = len(N)
a = int(N[0])
b = 11-int(N[0])
for i in range(n-1):
    a1 = min(a+int(N[i+1]), b+int(N[i+1]))
    b1 = min(a+11-int(N[i+1]), b+9-int(N[i+1]))
    a = a1
    b = b1
print(min(a,b))
