n = int(input())
div = [1, ]
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        div.append(i)
m = div[-1]
if m == 1:
    print((len(str(n))))
else:
    print((max(len(str(n // m)), len(str(m)))))
