n, p, k = map(int, input().split())
print("{} {} ({}) {} {}".format("<<" if p - k > 1 else "", \
  " ".join(map(str, range(max(1, p - k), p))), p,
  " ".join(map(str, range(p + 1, min(n, p + k) + 1))),
  ">>" if p + k < n else "").strip())
