N = int(input())
ls = list(map(int, input().split()))
print(min([ls[i] // max(i, N - i - 1) for i in range(N)]))
