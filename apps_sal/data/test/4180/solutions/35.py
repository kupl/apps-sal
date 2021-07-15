N = int(input())
if N%1000==0:
    print((0))
else:
    S = N // 1000
    print(((S+1)*1000-N))

