(A, B) = map(int, input().split())
p = 0.08
a = 0 - -A // p
b = (A + 1) // p
c = B * 10
d = c + 10
print([int(max(a, c)), -1][(d <= a) | (b <= c)])
