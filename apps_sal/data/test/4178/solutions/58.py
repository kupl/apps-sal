N = int(input())
H = list(map(int, input().split()))
can = True
for i in reversed(range(1, N)):
    if H[i - 1] - 1 == H[i]:
        H[i - 1] -= 1
    elif H[i - 1] - 1 > H[i]:
        can = False
        break
print(['No', 'Yes'][can])
