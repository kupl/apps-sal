modulus = 10**9 + 7

n, x = list(map(int, input().split()))
s = list(map(int, input().split()))

tot = sum(s)
powers = [tot - x for x in s]
powers.sort(reverse=True)

while True:

    low = powers[-1]
    cnt = 0
    while len(powers) > 0 and powers[-1] == low:
        cnt += 1
        powers.pop()
    if cnt % x == 0:
        cnt = cnt // x
        for n in range(cnt):
            powers.append(low + 1)
    else:
        low = min(low, tot)
        print(pow(x, low, modulus))
        return
