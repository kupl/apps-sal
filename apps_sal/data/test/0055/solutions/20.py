import math
x, k = list(map(int, input().split()))
kori = k
a = bin(x)

# s = a[2:len(a)]
qtz = 0
s = []
for i in range(2, len(a)):
    if a[i] == "1":
        k -= 1
        s.append(1)
    else:
        qtz += 1
        s.append(0)


v = []
for i in range(len(s)):
    if s[i] != 0:
        v.append((len(s) - 1) - i)
    # else:
        # v.append("x")

# print(qtz, k)
if k < 0:
    print("No")
    return
else:
    tam = len(s)
    # print(tam)
    print("Yes")
    # print(k, s)
    if k > 0:
        p = 0
        # diminui o y máximo
        while(1):
            # print(p, s[p], len(s))
            if tam - 1 <= p:
                s.append(0)
            if s[p] > k:
                break
            else:
                k -= s[p]
                s[p + 1] += s[p] * 2
                s[p] = 0
                p += 1
        # se k ainda for maior que zero
        if k > 0:
            j = len(s) - 1
            while k > 0:
                while s[j] == 0:
                    j -= 1
                s[j] -= 1
                if j == len(s) - 1:
                    s.append(2)
                    j += 1
                else:
                    s[j + 1] += 2
                    j += 1
                k -= 1

            # print(s)
        v = []
        for i in range(len(s)):
            for j in range(s[i]):
                v.append((tam - 1) - i)
        print(*v)
    else:
        v = []
        for i in range(len(s)):
            for j in range(s[i]):
                v.append(len(s) - 1 - i)
        print(*v)
