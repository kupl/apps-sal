N = int(input())


def divider(n):
    dividers = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            dividers.append(i)
            if i != n // i:
                dividers.append(n // i)
    dividers.sort()
    dividers.remove(1)
    return dividers
# nの約数を抽出する関数を定義(1以外)


cnt = len(divider(N - 1))
for k in divider(N):
    n = N
    while n % k == 0:
        n /= k
    if n % k == 1:
        cnt += 1
print(cnt)
