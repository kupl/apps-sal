dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

N = int(input())
P = {d: [] for d in dirs}
for i in range(N):
    x, y, d = input().split()
    x, y = list(map(int, (x, y)))
    P[d].append((x, y))

def fst(x): return x[0]
def snd(x): return x[1]
inf = float('inf')

# 方向別のX・Yの最大最小
S = {d: {'xmin': min(list(map(fst, P[d])), default= inf),
         'xmax': max(list(map(fst, P[d])), default=-inf),
         'ymin': min(list(map(snd, P[d])), default= inf),
         'ymax': max(list(map(snd, P[d])), default=-inf) }
     for d in dirs}

# 変化がある時刻は0と以下のt1, t2, t3
# S[L][xmax] - t1 == max(S[U][xmax], S[D][xmax]), t < t1 -> S[UD] < S[L]
# S[R][xmax] + t2 == max(S[U][xmax], S[D][xmax]), t < t2 -> S[R]  < S[UD]
# S[L][xmax] - t3 == S[R][xmax] + t3,             t < t3 -> S[R]  < S[L]

dirs = {d: {'x': dirs[d][0], 'y': dirs[d][1]} for d in dirs}
vars = ('xmax', 'xmin', 'ymax', 'ymin')
maxmin = {'max': max, 'min': min}
maxmin = {v: maxmin[v[-3:]] for v in vars}

# 変化がある時刻の集合
T = set()
T.add(0)
for v in vars:
    u, d, c1, c2 = ('R', 'L', 'U', 'D') if v.startswith('x') else \
                   ('U', 'D', 'R', 'L')
    C  = maxmin[v](S[c1][v], S[c2][v])
    t1 =  S[d][v] - C  # inf - inf == nan
    t2 = -S[u][v] + C
    t3 = (S[d][v] - S[u][v]) / 2
    T.update([t1, t2, t3])

# 各時刻のxmax, xmin, ymax, yminを計算
q = inf
for t in (t for t in T if 0 <= t < inf):
    Q = {v: maxmin[v](S[d][v] + t * dirs[d][v[0]] for d in dirs)
         for v in vars}
    q = min(q, (Q['xmax'] - Q['xmin']) * (Q['ymax'] - Q['ymin']))

print(q)

