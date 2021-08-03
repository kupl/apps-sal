S = input()
W = ['Sunny', 'Cloudy', 'Rainy']
i = W.index(S)
if i == 2:
    ans = 0
else:
    ans = i + 1
print(W[ans])
