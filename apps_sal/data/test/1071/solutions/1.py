a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
n = int(input())
n -= (a1 + a2 + a3 - 1) // 5 + 1
n -= (b1 + b2 + b3 - 1) // 10 + 1
print('YES' if n >= 0 else 'NO')
