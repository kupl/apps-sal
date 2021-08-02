print("%.8f" % (lambda a, b, c, d: a / b / (1 - (1 - a / b) * (1 - c / d)))(*list(map(int, input().split()))[0:4]))
