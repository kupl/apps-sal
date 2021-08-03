A = list(map(int, input().split()))
A = sorted(A, reverse=True)
print(int("".join(map(str, A[:2]))) + A[-1])
