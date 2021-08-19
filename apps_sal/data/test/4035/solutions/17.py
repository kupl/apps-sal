(A, B) = map(int, input().split())
a = 0 - -A * 25 // 2
b = (A + 1) * 25 // 2
c = B * 10
d = c + 10
print([int(max(a, c)), -1][(d <= a) | (b <= c)])
