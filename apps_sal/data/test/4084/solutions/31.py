N, A, B = map(int, input().split())

sho = N // (A + B)
amari = N % (A + B)

if amari >= A:
    ans = sho * A + A
else:
    ans = sho * A + amari

print(ans)
