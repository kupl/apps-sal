(n, k) = list(map(int, input().split()))
s = list(input()[::-1]) * 2
ptn = ['PR', 'RS', 'SP', 'RP', 'SR', 'PS', 'PP', 'RR', 'SS']
for _ in range(k):
    tmp = []
    while s:
        win = ptn.index(s.pop() + s.pop()) % 3
        tmp.append(['P', 'R', 'S'][win])
    s = tmp[::-1] * 2
print(s.pop())
