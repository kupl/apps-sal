MAX=200000
def get_prime(x):
  is_prime = [True] * 200000
  for i in range(2,MAX):
    if is_prime[i] and i >= x:
      return i
    elif is_prime[i]:
      for j in range(2 * i, MAX, i):
        is_prime[j] = False

print((get_prime(int(input()))))

