S = str(input())

zero = S.count('0')
one = S.count('1')

ans = min(zero,one)
print(ans*2)
