
n = int(input())
a_ = 2
a = 1
for i in range(n - 1):
    a, a_ = a + a_, a
print(a)
