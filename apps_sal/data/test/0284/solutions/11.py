HOUSE = 1234567
CAR = 123456
COMP = 1234
n = int(input())
answer = 'NO'
for h in range(n // HOUSE + 1):
    rest = n - h * HOUSE
    for c in range(rest // CAR + 1):
        rest2 = rest - c * CAR
        if rest2 % COMP == 0:
            answer = 'YES'
            break
print(answer)
