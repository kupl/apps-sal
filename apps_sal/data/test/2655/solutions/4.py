N = int(input())
*A, = sorted(map(int, input().split()), reverse=True)

print(sum([A[i // 2] for i in range(1, N)]))
