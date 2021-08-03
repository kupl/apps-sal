f0 = "What are you doing at the end of the world? Are you busy? Will you save us?"
f1 = "What are you doing while sending \"{0}\"? Are you busy? Will you send \"{0}\"?"
a = list(f1.split("{0}"))
b = list(map(len, a))
q = int(input())
def f(n): return 143 * 2**min(n, 54) - 68


for _ in range(q):
    n, k = map(int, input().split())
    ans = ""
    while n > 0 and b[0] < k < b[0] + f(n - 1):
        k -= b[0]
        n -= 1
    while not ans:
        w = f(n - 1)
        if k > f(n):
            ans = "."
        elif n == 0:
            ans = f0[k - 1]
        elif k <= b[0]:
            ans = a[0][k - 1]
        elif k <= b[0] + w:
            k -= b[0]
            n -= 1
        elif k <= b[0] + w + b[1]:
            k -= b[0] + w
            ans = a[1][k - 1]
        elif k <= b[0] + w + b[1] + w:
            k -= b[0] + w + b[1]
            n -= 1
        else:
            k -= b[0] + w + b[1] + w
            ans = a[2][k - 1]
    print(ans, end="")
