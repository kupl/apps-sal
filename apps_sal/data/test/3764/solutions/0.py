n, k, x = list(map(int, input().split()))
rangers = list(map(int, input().split()))

for i in range(min(k, 8 + k%4)):
    rangers.sort()
    rangers = [ rangers[i] if i%2 else rangers[i]^x for i in range(n)]
#    print(rangers)      

rangers.sort()
print(rangers[-1], rangers[0])

