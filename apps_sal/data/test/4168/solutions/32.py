N = int(input())
ans = []
if N == 0:
    print((0))
else:
    while N:
        ans.append(N % 2)
        N = -(N // 2)
    print(("".join(map(str, ans[::-1]))))
