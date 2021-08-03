t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0
    k = 1
    while n >= 10**k:
        answer += 9
        k += 1
    n %= 10**k
    i = 1
    while n >= int(str(i) * (k)):
        answer += 1
        i += 1

    print(answer)
