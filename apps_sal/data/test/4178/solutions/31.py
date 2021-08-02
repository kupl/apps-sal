N = int(input())
H = list(map(int, input().split()))
D = 0

for n in range(N):
    if D > H[n]:
        print("No")
        return
    elif D <= H[n] - 1:
        H[n] -= 1
        D = H[n]

print("Yes")
