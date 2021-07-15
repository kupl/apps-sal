n=int(input())
f=0
for i in range(15):
    for j in range(26):
        if n==7*i+j*4:
            f=1
print('Yes'if f else 'No')
