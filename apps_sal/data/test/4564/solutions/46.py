import sys
S = input()

for s in S:
    if S.count(s) > 1:
        print('no')
        return
        
print('yes')
