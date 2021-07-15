import sys
input = sys.stdin.readline
N,A,B,C = map(int,input().split())
S = [input().rstrip() for i in range(N)]

if A==B==C==0:
    print('No')
    return

if A+B+C == 1:
    ans = []
    for s in S:
        if (s=='AB' and A+B==0) or (s=='AC' and A+C==0) or (s=='BC' and B+C==0):
            print('No')
            return
        if s=='AB':
            if A<B:
                ans.append('A')
            else:
                ans.append('B')
            A,B = B,A
        if s=='AC':
            if A<C:
                ans.append('A')
            else:
                ans.append('C')
            A,C = C,A
        if s=='BC':
            if B<C:
                ans.append('B')
            else:
                ans.append('C')
            B,C = C,B
    print('Yes')
    print(*ans, sep='\n')

else:
    ans = []
    for i,s in enumerate(S):
        if (s=='AB' and A+B==0) or (s=='AC' and A+C==0) or (s=='BC' and B+C==0):
            print('No')
            return
        if s=='AB':
            if A==0:
                ans.append('A')
                A += 1
                B -= 1
            elif B==0:
                ans.append('B')
                B += 1
                A -= 1
            elif A==B==1:
                if i == N-1 or C > 0 or S[i+1]=='AB':
                    ans.append('A')
                    A += 1
                    B -= 1
                elif S[i+1]=='AC':
                    ans.append('A')
                    A += 1
                    B -= 1
                else:
                    ans.append('B')
                    B += 1
                    A -= 1
            elif A < B:
                ans.append('A')
                A += 1
                B -= 1
            else:
                ans.append('B')
                B += 1
                A -= 1
        if s=='AC':
            if A==0:
                ans.append('A')
                A += 1
                C -= 1
            elif C==0:
                ans.append('C')
                C += 1
                A -= 1
            elif A==C==1:
                if i == N-1 or B > 0 or S[i+1]=='AC':
                    ans.append('C')
                    C += 1
                    A -= 1
                elif S[i+1]=='AB':
                    ans.append('A')
                    A += 1
                    C -= 1
                else:
                    ans.append('C')
                    C += 1
                    A -= 1
            elif C < A:
                ans.append('C')
                C += 1
                A -= 1
            else:
                ans.append('A')
                A += 1
                C -= 1
        if s=='BC':
            if B==0:
                ans.append('B')
                B += 1
                C -= 1
            elif C==0:
                ans.append('C')
                C += 1
                B -= 1
            elif B==C==1:
                if i == N-1 or A > 0 or S[i+1]=='BC':
                    ans.append('B')
                    B += 1
                    C -= 1
                elif S[i+1]=='AB':
                    ans.append('B')
                    B += 1
                    C -= 1
                else:
                    ans.append('C')
                    C += 1
                    B -= 1
            elif B < C:
                ans.append('B')
                B += 1
                C -= 1
            else:
                ans.append('C')
                C += 1
                B -= 1
    print('Yes')
    print(*ans, sep='\n')
