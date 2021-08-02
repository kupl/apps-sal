a = int(input())
if a <= 2: print(-1)
else: print(' '.join(list(map(str, list(range(1, a + 1))))[::-1]))
