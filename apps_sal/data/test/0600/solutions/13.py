a = int(input())
b = int(input())
dist = abs(a - b)
t1 = dist // 2
t2 = (dist + 1) // 2
print(t1 * (t1 + 1) // 2 + t2 * (t2 + 1) // 2)
