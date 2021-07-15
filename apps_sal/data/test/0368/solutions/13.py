import sys
# sys.stdin = open('in.txt')
R = lambda: map(int, input().split())

score={'q':9, 'r':5, 'b':3, 'n':3, 'p':1, 'k':0,
       'Q':-9,'R':-5,'B':-3,'N':-3,'P':-1,'K':0, '.':0}

sum=0
for _ in range(8):
    for c in input():
        sum+=score[c]

if sum==0:
    print("Draw")
elif sum>0:
    print("Black")
else:
    print("White")
