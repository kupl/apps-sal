A, B, C = map(int, input().split())
Max = max(A, B, C)
K = int(input())
Max *= 2**K
print(min((A + B + Max), (A + Max + C), (Max + B + C)))
