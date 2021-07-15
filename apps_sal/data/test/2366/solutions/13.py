from collections import Counter

n = int(input())
a_array = list(map(int, input().split()))
a_counter = Counter(a_array)
count_max = max(a_counter.values())

def nC2(n):
    return n * (n - 1) // 2

nc2_array = [0] * (count_max + 1)
sum_comb = 0
for a, count in a_counter.items():
    comb = nC2(count)
    sum_comb += comb
    nc2_array[count] = comb
    nc2_array[count - 1] = nC2(count - 1)

for a in a_array:
    a_count = a_counter[a]
    ans = sum_comb - nc2_array[a_count] + nc2_array[a_count - 1]
    print(ans)
