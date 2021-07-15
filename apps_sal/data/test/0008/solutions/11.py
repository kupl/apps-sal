from sys import stdin, stdout

#N = int(input())

#arr = [int(x) for x in stdin.readline().split()]

s = input()

s = s.split(' ')

#print(s)

M = [0]*9
P = [0]*9
S = [0]*9

for pile in s:
    pile = list(pile)
    #print(pile)
    num = int(pile[0])
    tile = pile[1]
    
    if tile=='s':
        S[num-1] += 1
    elif tile=='p':
        P[num-1] += 1
    elif tile=='m':
        M[num-1] += 1
        
for i in range(9):
    if M[i]==3:
        print(0)
        quit()
    if P[i]==3:
        print(0)
        quit()
    if S[i]==3:
        print(0)
        quit()
        
for i in range(7):
    if M[i]==1 and M[i+1]==1 and M[i+2]==1:
        print(0)
        quit()
    if P[i]==1 and P[i+1]==1 and P[i+2]==1:
        print(0)
        quit()
    if S[i]==1 and S[i+1]==1 and S[i+2]==1:
        print(0)
        quit()

for i in range(9):
    if M[i]==2:
        print(1)
        quit()
    if P[i]==2:
        print(1)
        quit()
    if S[i]==2:
        print(1)
        quit()
        
for i in range(8):
    if M[i]==1 and M[i+1]==1:
        print(1)
        quit()
    if P[i]==1 and P[i+1]==1:
        print(1)
        quit()
    if S[i]==1 and S[i+1]==1:
        print(1)
        quit()
        
for i in range(7):
    if M[i]==1 and M[i+2]==1:
        print(1)
        quit()
    if P[i]==1 and P[i+2]==1:
        print(1)
        quit()
    if S[i]==1 and S[i+2]==1:
        print(1)
        quit()
        
print(2)
        
    

