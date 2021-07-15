# import time
N = input()
n = len(N)
# t1 = time.time()
# ぴったり払う:a 余分に払う:b
a = int(N[0])
b = 11-int(N[0])
# t2 = time.time()
for i in range(n-1):
    a1 = min(a+int(N[i+1]), b+int(N[i+1]))
    b1 = min(a+11-int(N[i+1]), b+9-int(N[i+1]))
    a = a1
    b = b1
print((min(a,b)))
# t3 = time.time()

# print(t2-t1,t3-t2)

