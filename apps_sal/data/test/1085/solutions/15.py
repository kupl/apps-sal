N=int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return (lower_divisors + upper_divisors[::-1])[1:]

F = make_divisors(N)
count = 0
for f in F:
  n = N
  while 1:
    if n % f != 0:
      n = n % f
    else:
      n = n // f
    if n < f:
      break
  if n == 1: count += 1
print(count + len(make_divisors(N-1)))
