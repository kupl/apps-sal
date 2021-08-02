N = int(input())

if N == 0:
    print((0))
    return
ans = []
while N:
    ans.append(N % 2)
    N = N // 2
    N *= -1

print(("".join(map(str, ans[::-1]))))
