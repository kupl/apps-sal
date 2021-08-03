N, Z, W = list(map(int, input().split()))
A = list(map(int, input().split()))
idea = abs(A[-1] - W)
try:
    idea2 = abs(A[-2] - A[-1])
except:
    print(idea)
    return
print((max(idea, idea2)))
