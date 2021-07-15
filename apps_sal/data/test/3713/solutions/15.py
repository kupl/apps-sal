n, s = int(input()), input()
print(min(n, s.count("01") + s.count("10") + 3))
