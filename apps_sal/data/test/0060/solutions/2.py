s = input()
n, p = int(s[:-1]), s[-1]
T = 16 * ((n - 1) // 4)
k = (n - 1) % 4 + 1
if k in (2, 4):
    T += 7
D = {'f': 1, 'e': 2, 'd': 3, 'a': 4, 'b': 5, 'c': 6}
T += D[p]
print(T)
