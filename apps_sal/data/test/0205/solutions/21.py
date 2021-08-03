import math
from decimal import Decimal


def list_int_input(inp): return list(map(int, inp.split()))
def int_input(inp): return int(inp)
def string_to_list_input(inp): return list(inp)


n, b = list(map(int, input().split()))
facts = []
sqt = int(math.sqrt(b))
for i in range(2, sqt + 1):
    j = 0
    while b % i == 0:
        j += 1
        b = int(Decimal(b) / Decimal(i))
    if j > 0:
        facts.append((i, j))
    if b == 1:
        break
if b != 1:
    facts.append((b, 1))
summ = 10**18
for i in facts:
    num = i[0]
    times = i[1]
    cnt = 0
    while int(n / num) != 0:
        cnt += int(Decimal(n) / Decimal(num))
        num *= i[0]
    summ = min(summ, int(Decimal(cnt) / Decimal(times)))
print(summ)
