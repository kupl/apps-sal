def prime_factorization(n):
    for i in range(2, n + 1):
        num = int(i ** 0.5)
        for prime in range(2, num + 2):
            if i % prime == 0:
                cnt = 0
                while True:
                    if i % prime != 0:
                        break
                    cnt += 1
                    i = i // prime
                if rec.get(prime):
                    rec[prime] += cnt
                else:
                    rec[prime] = cnt
        if i != 1:
            if rec.get(i):
                rec[i] += 1
            else:
                rec[i] = 1


n = int(input())
rec = dict()
prime_factorization(n)
dic = {2: 0, 4: 0, 14: 0, 24: 0, 74: 0}
cnt = 0
for (key, val) in rec.items():
    if val >= 2:
        dic[2] += 1
    if val >= 4:
        dic[4] += 1
    if val >= 14:
        dic[14] += 1
    if val >= 24:
        dic[24] += 1
    if val >= 74:
        dic[74] += 1
for i in [74, 24, 14, 4]:
    temp = dic.get(i)
    if i == 74:
        cnt += temp
    elif i == 24:
        cnt += temp * (dic[2] - 1)
    elif i == 14:
        cnt += temp * (dic[4] - 1)
    else:
        cnt += (dic[2] - 2) * (temp - 1) * temp // 2
print(cnt)
