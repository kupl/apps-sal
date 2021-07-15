n, x = list(map(int, input().split()))
a = abs(sum(list(map(int, input().split()))))
a = (a + x - 1) // x
print(a)

