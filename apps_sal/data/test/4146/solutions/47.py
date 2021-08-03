import collections
n = int(input())
a = [int(x) for x in input().split()]
even = []
uneven = []
for i in range(n):
    if i % 2 == 0:
        uneven.append(a[i])
        continue
    even.append(a[i])

uneven_counter = collections.Counter(uneven)
sortede_uneven_counter = sorted(uneven_counter.items(), key=lambda x: x[1], reverse=True)
even_counter = collections.Counter(even)
sortede_even_counter = sorted(even_counter.items(), key=lambda x: x[1], reverse=True)

ans = (n / 2 - sortede_uneven_counter[0][1]) + (n / 2 - sortede_even_counter[0][1])

if sortede_uneven_counter[0][0] == sortede_even_counter[0][0]:
    if len(set(a)) == 1:
        ans = n / 2
    elif sortede_uneven_counter[0][0] == sortede_even_counter[0][0]:
        ans = (n / 2 - sortede_uneven_counter[1][1]) + (n / 2 - sortede_even_counter[0][1])
        ans2 = (n / 2 - sortede_uneven_counter[0][1]) + (n / 2 - sortede_even_counter[1][1])
        if ans2 < ans:
            ans = ans2

print(int(ans))
