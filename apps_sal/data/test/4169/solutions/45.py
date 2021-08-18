def input2():
    return map(int, input().split())


def input_array():
    return list(map(int, input().split()))


n, m = input2()
AB = [input_array() for _ in range(n)]

AB = sorted(AB, key=lambda x: x[0])
ans = 0

for i in range(n):
    a = AB[i][0]
    b = AB[i][1]
    if b > m:
        ans += a * m
        break
    elif b == m:
        ans += a * b
        break
    else:
        ans += a * b
    m -= b
print(ans)
