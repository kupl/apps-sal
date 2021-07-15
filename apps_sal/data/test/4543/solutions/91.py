a,b=input().split()
s=0
s += int(b)
s += int(a)*(10**len(b))
for i in range(320):
    if s==i*i:
        print('Yes')
        return
print('No')

