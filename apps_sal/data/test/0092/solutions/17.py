p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def d(x):
    y = 0
    ans = 1
    for i in p:
        if x < i:
            break
        y = 1
        while x % i == 0 and x >= i:
            x /= i
            y += 1
        ans *= y
    return ans


(a, b, c) = list(map(int, input().split()))
out = 0
q = {}
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            e = i * j * k
            if e not in q:
                q[e] = d(e)
            out += q[e]
print(out % 1073741824)
