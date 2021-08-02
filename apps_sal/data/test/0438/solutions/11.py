n = int(input())
k = 0
size = n
for i in range(1, size + 1):
    n -= i
    k += 1
    if n <= i: break

print(k)
L = size
for i in range(1, L + 1):
    if size - i <= i:
        print(size)
        break
    print(i, end=" ")
    size -= i
