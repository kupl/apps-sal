s = input()
w = ['Sunny', 'Cloudy', 'Rainy']
if w.index(s) == 2:
    print(w[0])
else:
    print(w[w.index(s) + 1])
