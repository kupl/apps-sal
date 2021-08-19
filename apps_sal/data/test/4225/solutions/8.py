N = list(map(int, input().split()))
if N[0] >= N[3]:
    print(N[3])
elif N[1] >= N[3] - N[0]:
    print(N[0])
else:
    print(N[0] - (N[3] - N[0] - N[1]))
