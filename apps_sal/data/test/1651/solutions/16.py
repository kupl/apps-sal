S, P = map(int, input().split())


def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


D = divisor(P)

for d in D:
    tmp = P // d
    if tmp + d == S:
        print("Yes")
        return
else:
    print("No")
