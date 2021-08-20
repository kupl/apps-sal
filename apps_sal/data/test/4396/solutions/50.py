N = int(input())
m = []
for i in range(N):
    (x, u) = input().split(' ')
    if u == 'JPY':
        m.append(int(x))
    elif u == 'BTC':
        m.append(float(x) * 380000)
print(sum(m))
