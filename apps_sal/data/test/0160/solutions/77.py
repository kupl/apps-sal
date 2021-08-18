from collections import deque


def check(d: int):
    """ K回以下の操作でAがdの倍数となるか判定する """
    mod = deque(sorted([a % d for a in A if (a % d != 0)]))

    ans = 0
    while mod:
        modmin = mod.popleft()

        ans += modmin
        while modmin:
            if not mod:
                return False
            modmax = mod.pop()
            sub = d - modmax
            if sub <= modmin:
                modmin -= sub
            else:
                modmax += modmin
                if modmax % d != 0:
                    mod.append(modmax)
                modmin = 0

    return True if (ans <= K) else False


def make_divisors(n: int):
    """ nの約数を昇順で列挙 """
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


N, K = map(int, input().split())
A = [int(i) for i in input().split()]

sumA_divisors = make_divisors(sum(A))

ans = 0
for d in sumA_divisors:
    if check(d):
        ans = d

print(ans)
