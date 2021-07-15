# Nを１位上９以下の2つの整数の積として表せるならYes,できないならNo
N = int(input())

for i in range(1, 9+1):
    if N%i == 0 and N//i <= 9:
        print('Yes')
        return

print('No')
