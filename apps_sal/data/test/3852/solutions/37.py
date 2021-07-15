N, = list(map(int, input().split()))
As = list(map(int, input().split()))
a,b = max(As), min(As)
ai = As.index(a)
bi = As.index(b)
print((N-1+N-1))
if a > -b:
    for i in range(N):
        if i != ai:
            print((ai+1, i+1))
    for i in range(N-1):
        print((i+1, i+2))
else:
    for i in range(N):
        if i != bi:
            print((bi+1, i+1))
    for i in range(N-1):
        print((N-i, N-i-1))

