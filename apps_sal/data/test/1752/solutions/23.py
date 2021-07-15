n = int(input())
L = sorted(list(map(int, input().split())))
M = L[::2]
N = L[1::2][::-1]
print(*(M + N))
