T = ['Sunny', 'Cloudy', 'Rainy']
S = input()
idx = T.index(S)
print(T[idx + 1] if idx != 2 else T[0])
