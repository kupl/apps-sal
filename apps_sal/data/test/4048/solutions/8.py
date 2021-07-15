N = int(input())
ans = 10 ** 12 + 1
for a in range(1, int(N ** 0.5 + 2)):
    if N % a == 0:
        a_b = a + (N // a) - 2
    if ans > a_b:
        ans = a_b

print(int(ans))
