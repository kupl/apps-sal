n = int(input())
H = list(map(int, input().split()))
for i in range(1, n - 1):
    if H[i - 1] < H[i]:
        H[i] -= 1
    if H[i] > H[i + 1]:
        print("No")
        break
else:
    print("Yes")
