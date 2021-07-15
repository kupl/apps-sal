nk = list(map(int, input().split()))
n, k = nk[0], nk[1]
digit = 0

while n > k ** digit - 1:
    digit += 1

print(digit)

