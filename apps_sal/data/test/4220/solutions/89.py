N = int(input())
K = str(input())
x = K[:N]
 
if N < len(K):
    print(x+'...')
else:
    print(x)
