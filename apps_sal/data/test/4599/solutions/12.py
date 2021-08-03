N = int(input())
a = list(map(int, input().split()))


def sort_reverse(n):
    n.sort(reverse=True)
    return n


N_Even = list(range(0, N, 2))
N_Odd = list(range(1, N, 2))
a1 = sort_reverse(a)
sum1 = 0
sum2 = 0

for i in N_Even:
    sum1 += a1[i]
for j in N_Odd:
    sum2 += a1[j]

print(sum1 - sum2)
