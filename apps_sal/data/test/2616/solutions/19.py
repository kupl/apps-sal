import sys
input = sys.stdin.readline
 
t = int(input())
letters = 'abcdefghijklmnopqrst'
 
for _ in range(t):
    l = int(input())
    b = list(map(int, input().split()))
    c = 0
    
    if max(b) == 1:
        if l%2==0:
            print('Second')
        else:
            print('First')
    else:
        for j in range(len(b)):
            if b[j] > 1:
                if c==0:
                    print('First')
                else:
                    print('Second')
                break
            else:
                c += 1
                c = c%2
