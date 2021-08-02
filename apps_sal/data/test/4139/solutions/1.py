import itertools

N = input()
N_len = len(N)
N_int = int(N)
ans = 0
for i in range(3, 10):
    target = list(itertools.product([3, 5, 7], repeat=i))
    for t in target:
        s = ''.join(map(str, t))
        a = int(s)
        if a <= N_int and s.count('3') and s.count('5') and s.count('7'):
            ans += 1
print(ans)
