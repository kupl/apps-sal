def calc(n, k):
    k -= 1
    a, b = 0, 1
    for i in range(1, n + 2):
        if k - i >= 0:
            k -= i
            b += 1
        else:
            break
    a += k
    return "".join(["b" if i == a or i == b else "a" for i in range(n)[::-1]])

T = int(input())
for _ in range(T):
    n, k = list(map(int, input().split()))
    print(calc(n, k))

