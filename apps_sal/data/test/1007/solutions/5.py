(k, p) = list(map(int, input().split()))
i = 1
S = 0
while k > 0:
    S += int(str(i) + str(i)[::-1])
    i += 1
    k -= 1
print(S % p)
