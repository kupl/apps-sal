N = int(input())

d = 2

ans = 0

while d*d <= N:
    if N % d != 0:
        d += 1
        continue
        # Nがdで割り切れないとき，何もせずdを一歩進める。例えば d = 4 のときは，それ以前に d = 2 の時でNを割り切ってしまっているので，N % 4 != 0 と出る。

    z = d

    while N % z == 0:
         N //= z
         z *= d

         ans += 1

    while N % d == 0:
        N //= d

if N != 1:
    ans += 1

print(ans)
