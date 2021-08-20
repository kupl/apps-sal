t = int(input())
alfa = []
for i in range(t):
    (ll, v, l, r) = list(map(int, input().split()))
    ans = ll // v
    ans -= r // v - (l - 1) // v
    alfa.append(str(ans))
print('\n'.join(alfa))
