N, D = map(int, input().split())
a = 2 * D + 1
if N % a == 0:
    ans = N // a
else:
    ans = N // a + 1
print(ans)
