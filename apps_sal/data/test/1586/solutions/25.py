n = int(input())
if n % 2 == 1:
    ans = 0
else:
    fs = [2 * 5 ** i for i in range(1, 41)]
    ans = 0
    for i in range(40):
        ans += n // fs[i]
print(ans)
