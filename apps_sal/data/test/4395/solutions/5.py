import itertools
N = int(input())
Color = input()
ans = float('inf')
for c in itertools.permutations(('R', 'G', 'B')):
    ctr = 0
    for i, v in enumerate(Color):
        if c[i%3] != v:
            ctr += 1
    if ctr < ans:
        ans = ctr
        Ans = ''.join([c[i%3] for i in range(N)])
print(ans)
print(Ans)
