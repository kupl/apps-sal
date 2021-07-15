a, b = list(map(int, input().split()))

bool_a = a % 3 == 0
bool_b = b % 3 == 0
bool_ab = (a + b) % 3 == 0

if bool_a or bool_b or bool_ab:
    print('Possible ')
else:
    print('Impossible ')

