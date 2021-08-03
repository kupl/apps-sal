N = int(input())
A = list(map(int, input().split()))

count = 0
for _ in range(30):
    for i in range(N):
        B = A[i] % 2
        if B == 1:
            break
        A[i] = A[i] // 2
    else:
        count += 1
        continue
    break
print(count)
