N = int(input())
P = list(map(int, input().split()))
count = 0
for i in range(1, N + 1):
    if P[i - 1] != i:
        count += 1
if count <= 2:
    print("YES")
else:
    print("NO")
