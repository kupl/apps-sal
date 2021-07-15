N = int(input())
h = list(map(int, input().split()))
step=0
steps=0
for i in range(N-1):
    if h[i+1] < h[i]+step:
        step=h[i]-h[i+1] +step
        steps+=step
    else:
        step=0
print(steps)
