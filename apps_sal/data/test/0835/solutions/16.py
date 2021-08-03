def possible(n, money):
    if n * B > nB:
        money = money - pB * (n * B - nB)
    if n * C > nC:
        money = money - pC * (n * C - nC)
    if n * S > nS:
        money = money - pS * (n * S - nS)
    if money < 0:
        return False
    else:
        return True


hb = str(input())
B = hb.count('B')
C = hb.count('C')
S = hb.count('S')
nB, nS, nC = [int(k) for k in input().split()]
pB, pS, pC = [int(k) for k in input().split()]
money = int(input())

exceeded = False
i = 0
while not exceeded:
    r = money
    if (2**i) * B > nB:
        r = r - pB * ((2**i) * B - nB)
    if (2**i) * C > nC:
        r = r - pC * ((2**i) * C - nC)
    if (2**i) * S > nS:
        r = r - pS * ((2**i) * S - nS)
    if r < 0:
        exceeded = True
        break
    i += 1
# number of burgers is in range [2^(i-1) to 2^i)
lo = 2**(i - 1)
high = 2**(i)
mid = int((lo + high) / 2)

while lo <= high:
    if possible(mid, money):
        lo = mid + 1
        mid = (lo + high) // 2
    else:
        high = mid - 1
        mid = (lo + high) // 2
print(lo - 1)
