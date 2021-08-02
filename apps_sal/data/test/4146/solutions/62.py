from collections import Counter
n = int(input())
v_lis = list(map(int, input().split()))

v_odd = [0] * (n // 2)
v_even = [0] * (n // 2)

for i in range(n):
    if (i + 1) % 2 == 1:
        v_odd[i // 2] += v_lis[i]
    else:
        v_even[i // 2] += v_lis[i]

v_odd, v_even = Counter(v_odd).most_common(), Counter(v_even).most_common()

if v_odd[0][0] != v_even[0][0]:
    cnt = v_odd[0][1] + v_even[0][1]

else:
    tmp1 = v_odd[0][1] + (v_even[1][1] if len(v_even) >= 2 else 0)
    tmp2 = v_even[0][1] + (v_odd[1][1] if len(v_odd) >= 2 else 0)
    cnt = max(tmp1, tmp2)

print(n - cnt)
