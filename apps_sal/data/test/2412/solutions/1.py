N = int(input())

for i in range(N):
    l = int(input())
    
    S = input()
    
    if '8' in S and len(S) - S.index('8') >= 11:
        print("YES")
    else:
        print("NO")
