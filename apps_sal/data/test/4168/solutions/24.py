N = int(input())
ans = []
while N != 0:
    r = N % 2
    N = (N - r) // -2
    ans += [r]
print(''.join(map(str, ans[::-1])) if ans else 0)
