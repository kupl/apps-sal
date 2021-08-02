n = int(input())
s = str(input())
k = 1
move = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U'}
plus = set()
for i in s:
    if i in plus:
        plus.clear()
        k += 1
    plus |= {move[i]}
print(k)
