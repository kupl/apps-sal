a = list(map(int, [input() for _ in range(2)][1].split()))
print(a[-1] ^ max(a))
