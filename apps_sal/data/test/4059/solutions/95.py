# def cin():
#     return list(map(int, input().split()))

# count = 0
# N = cin()[0]

# for i in range(1, N+1):
#     num = N - i
#     for j in range(1, N+1):
#         if num != 0 and num % j == 0:
#             count += 1
    
# print(count)
import math


def cin():
    return list(map(int, input().split()))

count = 0
N = cin()[0]

for A in range(1, N+1):
    B = math.floor(N / A)
    C = N % A
    
    if B != 0 and C != 0:
        count += B
    elif B != 0 and C == 0:
        count += B - 1
    
print(count)
