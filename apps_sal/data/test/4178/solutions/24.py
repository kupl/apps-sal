N = int(input())
H = list(map(int, input().split()))
B = H[::-1]
for i in range(N - 1):
    if B[i] < B[i + 1]:
        B[i + 1] -= 1
    if B[i] < B[i + 1]:
        print("No")
        return

print("Yes")
