A = []
x = 0
i = 1
while x <= 10 ** 11:
    x += 3 * i - 1
    A.append(x)
    i += 1
for i in range(int(input())):
    n = int(input())
    ans = 0
    k = int(n ** 0.5) + 1
    while n >= 0 and k >= 0:
        # print(k)
        if n < A[k]:
            k -= 1
        else:
            n -= A[k]
            ans += 1

    print(ans)
