k = int(input())
def gcd1 (a, b):
    while True:
        if (a < b):
            a, b = b, a
        c = a%b
        if (c == 0):
            return (b)
        else:
            a = b
            b = c

def gcd2 (a, b, c):
    tmp = gcd1(a, b)
    ans = gcd1(tmp, c)
    return (ans)

count = 0
for i in range(k):
    for j in range(i, k):
        for l in range(j, k):
            tmp = gcd2(i + 1, j + 1, l + 1)
            if (i == j == l):
                count = count + tmp
            elif (i == j or j == l):
                count = count + tmp*3
            else:
                count = count + tmp*6
print(count)

