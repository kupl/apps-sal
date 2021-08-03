N = input()
X = sum(list(map(int, list(N))))
if int(N) % X == 0:
    print('Yes')
else:
    print('No')
