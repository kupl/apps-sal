L = [(i + 1) * 9 * 10**i for i in range(12)]
number = int(input())

exponent = 0
while number >= 0:
    number -= L[exponent]
    exponent += 1
exponent -= 1
number %= L[exponent]
start = 10**exponent
numDigits = exponent + 1
final = start + (number // numDigits - 1)
remainder = number % numDigits
if remainder == 0:
    final = str(final)
    print(final[-1])
else:
    final = str(final + 1)
    print(final[remainder - 1])
'''print(number, exponent, numDigits, start, final, remainder)'''
