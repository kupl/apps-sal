(N, K) = map(int, input().split())
D = list(map(int, input().split()))
while True:
    S = str(N)
    flag = True
    for x in S:
        if int(x) in D:
            flag = False
    if flag == True:
        break
    N += 1
print(N)
