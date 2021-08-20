n = int(input())
num = 1
k = 2
l = [1]
while num < n:
    num = (2 ** k - 1) * 2 ** (k - 1)
    if n % num == 0:
        l.append(num)
    k += 1
print(l[-1])
