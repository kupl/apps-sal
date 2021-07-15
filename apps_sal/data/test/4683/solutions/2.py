def cumsum(xs):
  result = [xs[0]]
  for x in xs[1:]:
    result.append(result[-1] + x)
  return result

N = int(input())
A = list(map(int, input().split()))

ans = 0
MOD = 10**9 + 7
A.reverse()
ruisekiwa = cumsum(A)
ruisekiwa.reverse()
A.reverse()

for i in range(N-1):
        ans = (ans + A[i] * ruisekiwa[i+1]) % MOD

print(ans)
