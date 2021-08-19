N = int(input())
D = {}
D['A', 'A'] = str(input())
D['A', 'B'] = str(input())
D['B', 'A'] = str(input())
D['B', 'B'] = str(input())
Val = [{} for i in range(6)]
Val[0]['A', 'B'] = 1
for i in range(len(Val)):
    for (k, v) in Val[i - 1].items():
        K = list(k)
        for j in range(1, len(k)):
            A = K[0:j] + [D[K[j - 1], K[j]]] + K[j:]
            Val[i][tuple(A)] = 1
mod = 10 ** 9 + 7
if N <= 7:
    print(len(Val[-1 - (7 - N)]))
elif len(Val[-1]) == 1:
    print(1)
elif len(Val[-1]) == 8:
    L = [2, 3]
    for i in range(N - 5):
        L.append((L[-1] + L[-2]) % mod)
    print(L[-1])
else:
    print(pow(2, N - 3, mod))
