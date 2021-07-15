n = int(input())
h1 = list(map(int,input().split()))
h2 = list(map(int,input().split()))
if n > 1:
    h12 = [0] * n
    h22 = [0] * n
    h12[0] = h1[0]
    h22[0] = h2[0]
    h12[1] = max(h12[0],h22[0] + h1[1])
    h22[1] = max(h22[0],h12[0] + h2[1])
    for i in range(2,n):
        h12[i] = max(h12[i-1],h22[i-1] + h1[i])
        h22[i] = max(h22[i-1],h12[i-1] + h2[i])
        h12[i] = max(h12[i],h22[i-2] + h1[i])
        h22[i] = max(h22[i],h12[i-2] + h2[i])
    print(max(h12[-1],h22[-1]))
else:
    print(max(h1[0],h2[0]))

