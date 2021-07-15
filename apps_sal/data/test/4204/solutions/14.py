S = input()
K = int(input())

for i in range(K):
    if S[i] != '1':
        print((S[i]))
        return
    
    if i == K - 1:
        print('1')
        return



