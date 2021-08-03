with open(0) as f:
    R, G = map(int, f.read().split())
print(2 * G - R)
