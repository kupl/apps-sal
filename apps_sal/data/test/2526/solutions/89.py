X, Y, A, B, C = list(map(int, input().split()))
Ps = list(map(int, input().split()))
Qs = list(map(int, input().split()))
Rs = list(map(int, input().split()))

Ps.sort(reverse=True)
Qs.sort(reverse=True)
Rs += Ps[:X] + Qs[:Y]

Rs.sort(reverse=True)

ans = sum(Rs[:X+Y])
print(ans)

