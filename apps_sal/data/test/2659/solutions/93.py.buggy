def snu(n):
    s = str(n)
    kei = sum(int(x) for x in s)
    return n / kei


def nn(n):
    s = str(n)
    kt = len(str(int(snu(n))))
    if s[-kt:].count("9") == kt:
        if s[-kt - 1] == "9":
            n += 10**kt
            s = str(n)
            kt = len(str(int(snu(n))))
            if s[-kt:].count("9") == kt:
                return n
            else:
                s = s[:-kt] + "9" * kt
                return int(s)
        else:
            return n + 10**kt
    else:
        s = s[:-kt] + "9" * kt
        return int(s)


k = int(input())
t = 9 if k > 9 else k
for i in range(1, t + 1):
    print(i)
if k <= 9:
    return
n = 19
for _ in range(k - 9):
    print(n)
    n = nn(n)
