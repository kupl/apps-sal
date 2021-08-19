(a1, a2, a3) = map(int, input().split())
(b1, b2, b3) = map(int, input().split())
n = int(input())
k = (a1 + a2 + a3 + 4) // 5 + (b1 + b2 + b3 + 9) // 10
s = 'YES' if k <= n else 'NO'
print(s)
