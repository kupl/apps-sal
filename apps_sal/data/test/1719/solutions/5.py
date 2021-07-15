N = int(input())

MOD = 10 ** 9 + 7

total = 4 ** N

if N == 3:
    sub = 3
    ans = total - sub
    
elif N >= 4:
    last_three = [{} for _ in range(N - 3 + 1)]
    for n in range(N - 3 + 1):
        for i in ['A', 'G', 'C', 'T']:
            for j in ['A', 'G', 'C', 'T']:
                for k in ['A', 'G', 'C', 'T']:
                    if [i, j, k] != ['A', 'G', 'C'] and [i, j, k] != ['A', 'C', 'G'] and [i, j, k] != ['G', 'A', 'C']:
                        last_three[n]["".join([i, j, k])] = 0
    for k in last_three[0].keys():
        last_three[0][k] = 1
    for i in range(4, N + 1):
        for k in last_three[i - 4].keys():
            if k[1] == 'A' and k[2] == 'G':
                last_three[i - 3]["".join([k[1], k[2], 'A'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'G'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'T'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'A'])] %= MOD
                last_three[i - 3]["".join([k[1], k[2], 'G'])] %= MOD
                last_three[i - 3]["".join([k[1], k[2], 'T'])] %= MOD
            elif k[1] == 'A' and k[2] == 'C':
                last_three[i - 3]["".join([k[1], k[2], 'A'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'C'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'T'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'A'])] %= MOD
                last_three[i - 3]["".join([k[1], k[2], 'C'])] %= MOD
                last_three[i - 3]["".join([k[1], k[2], 'T'])] %= MOD
            elif k[1] == 'G' and k[2] == 'A':
                last_three[i - 3]["".join([k[1], k[2], 'A'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'G'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'T'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'A'])] %= MOD
                last_three[i - 3]["".join([k[1], k[2], 'G'])] %= MOD
                last_three[i - 3]["".join([k[1], k[2], 'T'])] %= MOD
            elif k[0] == 'A' and k[2] == 'G':
                last_three[i - 3]["".join([k[1], k[2], 'A'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'G'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'T'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'A'])] %= MOD
                last_three[i - 3]["".join([k[1], k[2], 'G'])] %= MOD
                last_three[i - 3]["".join([k[1], k[2], 'T'])] %= MOD
            elif k[0] == 'A' and k[1] == 'G':
                last_three[i - 3]["".join([k[1], k[2], 'A'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'G'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'T'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'A'])] %= MOD
                last_three[i - 3]["".join([k[1], k[2], 'G'])] %= MOD
                last_three[i - 3]["".join([k[1], k[2], 'T'])] %= MOD
            else:
                last_three[i - 3]["".join([k[1], k[2], 'A'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'G'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'C'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'T'])] += last_three[i - 4][k] % MOD
                last_three[i - 3]["".join([k[1], k[2], 'A'])] %= MOD
                last_three[i - 3]["".join([k[1], k[2], 'G'])] %= MOD
                last_three[i - 3]["".join([k[1], k[2], 'C'])] %= MOD
                last_three[i - 3]["".join([k[1], k[2], 'T'])] %= MOD

    ans = sum(last_three[N - 3].values()) % MOD

print(ans)            
