from collections import Counter
n = int(input())
V = list(map(int, input().split()))
even = Counter(V[0::2])
even['0'] = 0
even = sorted(even.items(), key=lambda x: x[1], reverse=True)
odd = Counter(V[1::2])
odd['-1'] = 0
odd = sorted(odd.items(), key=lambda x: x[1], reverse=True)
i = 0
(even_top2, odd_top2) = ([], [])
for (e, o) in zip(even, odd):
    i += 1
    even_top2.append(e)
    odd_top2.append(o)
    if i == 2:
        break
if even_top2[0][0] != odd_top2[0][0]:
    notchange = even_top2[0][1] + odd_top2[0][1]
else:
    notchange = max(even_top2[0][1] + odd_top2[1][1], even_top2[1][1] + odd_top2[0][1])
print(n - notchange)
