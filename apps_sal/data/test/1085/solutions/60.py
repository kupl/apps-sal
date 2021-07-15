import copy
def make_divisors(n):
  divisors = []
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n // i)

  # divisors.sort()
  return divisors


n = int(input())

box = make_divisors(n-1)
ans = len(box)-1
boxn = make_divisors(n)
for i in range(1,len(boxn)):
    k = boxn[i]
    nn = copy.deepcopy(n)
    while nn % k == 0 and nn >= k:
        nn = nn // k

    if nn % k == 1:
        ans += 1

print(ans)

