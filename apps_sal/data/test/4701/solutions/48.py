n = int(input())
k = int(input())
numb = 1
for i in range(n):
    if 2 * numb < numb + k:
        numb *= 2
    else:
        numb += k
print(numb)
