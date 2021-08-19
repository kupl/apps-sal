from collections import Counter

S = input()
# S = "12345"*40000
N = len(S)

l = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    l[i] = (l[i + 1] + pow(10, N - i, 2019) * int(S[i])) % 2019
    # if i%10000 == 0:
    #     print(i)

# print(list(Counter(l).values()))

r = sum(m * (m - 1) // 2 for m in Counter(l).values())
print(r)
