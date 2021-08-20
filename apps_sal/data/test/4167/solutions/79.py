import sys
input = sys.stdin.readline
(N, K) = map(int, input().split())
multip_K = [i for i in range(K, N + 1, K)]
le = len(multip_K)
ans_mod_0 = le ** 3
ans_mod_haf = 0
if K % 2 == 0:
    multip_haf = [i for i in range(1, N + 1) if i % K == K // 2]
    le_haf = len(multip_haf)
    ans_mod_haf = le_haf ** 3
ans = ans_mod_0 + ans_mod_haf
print(ans)
