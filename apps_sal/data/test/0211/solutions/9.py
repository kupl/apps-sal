3

def modulo_power(modulo, power, base):
    if power == 0:
        return 1
    if power == 1:
        return base

    remainder = power % 2
    power -= remainder

    half = modulo_power(modulo, power/2, base)

    return (half * half * modulo_power(modulo, remainder, base)) % modulo

data = [int(token) for token in input().split()]
num_questions, num_correct, doubler = data

num_wrong = num_questions - num_correct
tail = num_wrong * (doubler - 1)
head = num_correct - tail

if head < 0:
    print(num_correct)
    return

num_doublings = head // doubler
remainder = head - num_doublings * doubler
modulo = 10**9 + 9
result = ((2 * doubler * (modulo_power(modulo, num_doublings, 2) - 1)) +
            remainder + tail) % modulo

print(result)


