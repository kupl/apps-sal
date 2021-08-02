N = int(input())
A = [str(i)for i in range(1, 10)]
ans = 0
for a in A:
    for b in A:
        countA = 0
        if a == b and int(a) <= N:
            countA += 1
        for i in range(5):
            m = int(a + '0' * i + b)
            M = int(a + '9' * i + b)
            if m <= N:
                if M <= N:
                    countA += 10**i
                else:
                    while m <= N:
                        countA += 1
                        m += 10

        countB = 0
        if b == a and int(b) <= N:
            countB += 1
        for i in range(5):
            m = int(b + '0' * i + a)
            M = int(b + '9' * i + a)
            if m <= N:
                if M <= N:
                    countB += 10**i
                else:
                    while m <= N:
                        countB += 1
                        m += 10

        ans += countA * countB
print(ans)
