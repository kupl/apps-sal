
def div_by_2(n):
    res = 0
    while n % 2 == 0:
        n //= 2
        res += 1
    return res

N = int(input())
A = list(map(int, input().split()))
print(min(map(div_by_2, A)))
