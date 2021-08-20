from itertools import count
n = int(input())
twos = 0
fives = 0
ans = []


def p_in_num(p, num):
    coun = 0
    while num % p == 0:
        num //= p
        coun += 1
    return coun


for i in count(2):
    twos += p_in_num(2, i)
    fives += p_in_num(5, i)
    zeroes = min(twos, fives)
    if zeroes == n:
        ans.append(i)
    elif zeroes > n:
        break
print(len(ans))
if len(ans) != 0:
    print(*ans)
