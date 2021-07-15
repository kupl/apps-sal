N = int(input())
A = list(map(int, input().split()))
M = len(set(A))

print(M if M % 2 else M - 1)
