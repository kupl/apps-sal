l, r = map(int, input().split())
hmm, t = l ^ r, 2 ** 60
while hmm ^ t > hmm:
  t //= 2
print(2 * t - 1 if hmm != 0 else 0)
