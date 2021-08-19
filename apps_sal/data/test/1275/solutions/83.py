n, k = list(map(int, input().split()))
kazu = [0] + [i for i in range(n + 1)]
rev_kazu = sorted(kazu[:n + 1], reverse=True)
kazu += rev_kazu
# print(kazu)
ans = 0
for A in range(2, 2 * n + 1):
    B = A - k
    if B >= 2 and B <= 2 * n:
        ans += kazu[A] * kazu[B]
print(ans)
