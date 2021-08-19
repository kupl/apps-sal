(A, B, C, D) = map(int, input().split())
second = min(B, D) - max(A, C)
if second < 0:
    print('0')
else:
    print(second)
