N = int(input())
if N < 1 or 1000 < N:
    print('数値が範囲外です')
elif N < 3:
    print(0)
else:
    print(N // 3)
