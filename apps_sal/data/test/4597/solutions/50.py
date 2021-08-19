import re
import copy


def accept_input():
    N = input()
    return int(N)


N = accept_input()
power = 1
for i in range(1, N + 1):
    power = power * i % (10 ** 9 + 7)
print(power)
