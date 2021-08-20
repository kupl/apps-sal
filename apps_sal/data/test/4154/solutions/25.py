(n, m) = map(int, input().split())
a_max = 1
b_min = n
for i in range(m):
    (a, b) = map(int, input().split())
    if a > a_max:
        a_max = a
    if b < b_min:
        b_min = b
print(max(0, b_min - a_max + 1))
