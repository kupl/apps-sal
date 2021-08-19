N = int(input())
H = [int(n) for n in input().split()]
reached = [False] * N
max_count = 0
for i in range(N):
    if reached[i] == True:
        continue
    else:
        count = 0
        for j in range(0, N - i - 1):
            if H[i + j + 1] <= H[i + j]:
                count += 1
                reached[i + j + 1] = True
            else:
                max_count = max(max_count, count)
                break
        else:
            max_count = max(max_count, count)
print(max_count)
