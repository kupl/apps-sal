(a, b, c, d) = list(map(int, input().split()))
print('{0:.10f}'.format(a / b / (1 - (1 - a / b) * (1 - c / d))))
