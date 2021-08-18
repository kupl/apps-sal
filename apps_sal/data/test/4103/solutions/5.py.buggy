nn, bb, aa = map(int, input().split())
n, b, a = nn, bb, aa
S = list(map(int, input().split()))
for i in range(n):
    if a == 0 and b == 0:
        print(i)
        return
    if S[i] == 1:
        if b > 0 and a < aa:
            b -= 1
            a += 1
        else:
            a -= 1
    else:
        if a > 0:
            a -= 1
        else:
            b -= 1
print(n)
