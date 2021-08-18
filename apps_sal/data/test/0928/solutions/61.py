import bisect
N, K = list(map(int, input().split()))
As = list(map(int, input().split()))

as_ruisekiwa = [0]

for a in As:
    as_ruisekiwa.append(a + as_ruisekiwa[-1])


ans = 0

for i in range(N + 1):
    index_check_num = K + as_ruisekiwa[i]
    index = bisect.bisect_left(as_ruisekiwa, index_check_num)
    ans += N - index + 1

print(ans)
