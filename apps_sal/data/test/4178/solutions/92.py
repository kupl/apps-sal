n = int(input())
H = list(map(int,input().split()))

for i in range(1,n-1):
    if H[n-1-i] == H[n-i] + 1:
        H[n-1-i] -= 1
    elif not(H[n-1-i] == H[n-i] or H[n-1-i] < H[n-i]):
        print('No')
        return
print('Yes')
