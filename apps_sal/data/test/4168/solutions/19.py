N = int(input())

ans = ""

if N == 0:
    print(0)
    return

while N != 0:
    a, b = divmod(N, 2)
    ans = str(b) + ans
    N = -a

print(ans)
