m, k = list(map(int, input().split()))

D = list(map(int, input().split()))

S = list(map(int, input().split()))

ans = 0

fuel = S[0]

maxx = S[0]

for i in range(m):

    if(D[i] > fuel):

        x = D[i] - fuel

        y = x // maxx

        if(x % maxx > 0):

            y += 1

        ans += y * k

        fuel += maxx * y

        fuel -= D[i]

        ans += D[i]

        if(i + 1 == m):

            break

        fuel += S[i + 1]

        maxx = max(S[i + 1], maxx)

    else:

        fuel -= D[i]

        ans += D[i]

        if(i + 1 == m):

            break

        fuel += S[i + 1]

        maxx = max(S[i + 1], maxx)

print(ans)
