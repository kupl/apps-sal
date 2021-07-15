N=int(input())
if 10<=N and N<=99:
    n=str(N)
    if (int(n[0])==9 or int(n[1])==9) or (int(n[0])==9 and int(n[1])==9):
        print('Yes')
    else:
        print('No')
