N = int(input())
if N % 2 == 1:
    ans = 0
else:
    div2 = N // 2
    n = N // 2
    k = 1
    while n // 2 ** k > 0:
        div2 += n // 2 ** k
        k += 1
    div5 = 0
    n = N // 2
    k = 1
    while n // 5 ** k > 0:
        div5 += n // 5 ** k
        k += 1
    ans = min(div2, div5)
print(ans)
