N = int(input())
A = list(map(int, input().split()))
median = sorted((a - i for (i, a) in enumerate(A)))[N // 2]
print(sum((abs(a - (median + i)) for (i, a) in enumerate(A))))
