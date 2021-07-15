def f(N):
    l = 0
    NN = N
    while True:
        l += 1
        NN //= 10
        if NN < 10:
            break
    m = N / sum(map(int,list(str(N))))
    num = -1
    for d in range(0,l+2):
        x = (10 ** (d+1)) * int(N/(10**(d+1))+1) - 1
        sx = sum(map(int,list(str(x))))
        value = x/sx
        if value < m:
            m = value
            num = d
    if num == -1:
        return N
    else:
        return (10 ** (num+1)) * int(N/(10**(num+1))+1) - 1

K = int(input())

N = 1
ans = [1]

while len(ans) < K:
    N = f(N+1)
    ans.append(N)

for i in ans:
    print(i)

