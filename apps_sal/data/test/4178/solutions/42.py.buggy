N = int(input())
H = [int(i) for i in input().split()]
for i in range(N - 1, 0, -1):
    if(H[i] < H[i - 1]):
        H[i - 1] -= 1
for i in range(N - 1):
    if(H[i] > H[i + 1]):
        print("No")
        return
print("Yes")
