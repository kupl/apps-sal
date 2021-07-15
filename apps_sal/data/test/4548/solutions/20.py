N, M, X = list(map(int, input().split()))
a_point = list(map(int,input().split()))
lg = 0
sl = 0
for i in range(len(a_point)):
    if X < a_point[i]:
        lg  += 1
    else:
        sl += 1

if lg > sl:
    print(sl)
else:
    print(lg)

