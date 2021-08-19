(a, b) = list(map(int, input().split()))
A = str(a)
B = str(b)
aaa = A * b
bbb = B * a
lists = sorted([aaa, bbb])
print(lists[0])
