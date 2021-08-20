3
n = input().strip()
print(max(list(map(int, [n, n[:-1], n[:-2] + n[-1]]))))
