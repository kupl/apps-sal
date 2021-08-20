def divisor(k):
    return (2 ** k - 1) * 2 ** (k - 1)


k = int(input().strip().split()[0])
answer = 1
for i in range(1, k):
    if divisor(i) > k:
        break
    elif k % divisor(i) == 0:
        answer = divisor(i)
print(answer)
