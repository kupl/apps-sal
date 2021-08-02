# Brute

n = int(input())
a = [int(i) for i in input().split()]
p = a[0]
a = a[1:]
w = 0

while p <= max(a):
    p += 1
    q = max(a)
    a.remove(q)
    a.append(q - 1)
    w += 1

print(w)
