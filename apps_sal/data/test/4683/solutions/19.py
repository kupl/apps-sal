N = int(input())
A = list(map(int, input().split()))
print((sum(A) ** 2 - sum((a ** 2 for a in A))) // 2 % (10 ** 9 + 7))
