N = int(input())

for cake in range(N):
    for dornat in range(N):
        if 4*cake + 7*dornat == N:
            print('Yes')
            return
        
print('No')
