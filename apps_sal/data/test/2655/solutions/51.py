N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

ans = 0

i = 0
nokori = N - 1
while nokori > 0:
    if i == 0:
        ans += A[i]
        nokori -= 1
    else:
        if nokori == 1:
            ans += A[i]
            nokori -= 1
        else:
            ans += 2 * A[i]
            nokori -= 2
    i += 1

print(ans)
