Q = int(input())
for _ in range(Q):
    N = int(input())
    X = []
    zeros = 0
    odds = 0
    for __ in range(N):
        s = input()
        odds += len(s) % 2
        zeros += s.count("0")
    
    if odds or (zeros % 2 == 0):
        print(N)
    else:
        print(N-1)

