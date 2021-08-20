N = int(input())
SP = []
idx = 1
for _ in range(N):
    (S, P) = input().split()
    SP.append([idx, S, int(P)])
    idx += 1
SP.sort(key=lambda x: (x[1], -x[2]))
for i in range(N):
    print(SP[i][0])
