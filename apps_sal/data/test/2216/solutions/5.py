n,m,k = list(map(int,input().split()))
unit_tube = (n * m) // k
long_tube = (n * m) % k + unit_tube

print(long_tube,end='')
i = 0
j = 0
ref = 0
for _ in range(long_tube):
    print(' {0} {1}'.format(i + 1,abs(j + 1 - ref)),end='')
    if((j + 1) % (m) == 0):
        i+=1
        ref = 0 if(ref) else m + 1
    j = (j + 1) % m
print()
for _ in range(k - 1):
    print(unit_tube,end='')
    for _ in range(unit_tube):
        print(' {0} {1}'.format(i + 1,abs(j + 1 - ref)),end='')
        if((j + 1) % (m) == 0):
            i+=1
            ref = 0 if(ref) else m + 1
        #j = abs((j + 1) % (m) - ref)
        j = (j + 1) % m
    print()
        
