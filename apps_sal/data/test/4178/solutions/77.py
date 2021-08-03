N = int(input())
H = list(map(int, input().split()))

maxh = 10 ** 10
for i in range(len(H) - 1, -1, -1):
    if H[i] > maxh + 1:
        print("No")
        break
    if H[i] == maxh + 1:
        maxh = H[i] - 1
    else:
        maxh = H[i]
else:
    print("Yes")
