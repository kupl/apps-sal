(N, K) = list(map(int, input().split()))
S = [tuple(map(int, input().split())) for _ in range(N)]
S.sort(key=lambda x: -x[1])
st = set()
(first_acc, other_acc) = ([0], [0])
for (t, d) in S:
    if t in st:
        other_acc.append(other_acc[-1] + d)
    else:
        st.add(t)
        first_acc.append(first_acc[-1] + d)
ans = 0
for i in range(K + 1):
    if len(first_acc) <= i or len(other_acc) <= K - i:
        continue
    ans = max(ans, first_acc[i] + other_acc[K - i] + i * i)
print(ans)
