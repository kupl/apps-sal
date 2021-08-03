(w, m, k) = (int(string) for string in input().split())
answer = 0
digitCount = len(str(m))
while w > 0:
    ceiling = 10**digitCount
    numberCountInThisLength = ceiling - m
    cost = digitCount * k * numberCountInThisLength
    if w > cost:
        w -= cost
        answer += numberCountInThisLength
        m = ceiling
        digitCount += 1
    else:
        answer += w / (k * digitCount)
        break

print('%d' % answer)
