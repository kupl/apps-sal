a=int(input())
a=bin(a+128)
print(32*int(a[4])+16*int(a[9])+8*int(a[7])+4*int(a[6])+2*int(a[8])+int(a[5]))
