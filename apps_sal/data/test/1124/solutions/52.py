n, *a = map(int, open(0).read().split())
b = min(a)
while sum(i % b for i in a):
    a = [i - i // b * b for i in a if i - i // b * b > 0]
    b = min(a)
print(b)
