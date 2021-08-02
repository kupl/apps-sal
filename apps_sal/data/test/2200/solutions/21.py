R = lambda: map(int, input().split())
n, a, b = R()
print(" ".join(map(str, (((w * a) % b) // a for w in R()))))
