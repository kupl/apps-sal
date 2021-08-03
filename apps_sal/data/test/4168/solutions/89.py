N = int(input())
ans = ""

if N == 0:
    print(0)
else:
    while N != 0:
        ans += str(N % 2)
        N = -(N // 2)
    print(ans[::-1])
