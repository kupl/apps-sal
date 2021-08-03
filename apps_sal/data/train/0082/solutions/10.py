
T = int(input())

#lets = 'abcdefghijklmnopqrstuvwxyz'
#key = {lets[i]:i for i in range(26)}

for t in range(T):
    n = int(input())
    #n,k = map(int,input().split())
    #a = list(map(int,input().split()))
    a = input().split()
    d = False
    a.reverse()
    print(' '.join(a))
