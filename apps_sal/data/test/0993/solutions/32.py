N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
AA = []
a_dict = {}
ans = 0
for a in A:
    num = a % M
    if len(AA) > 0:
        num = (num + AA[-1]) % M
    if not num in a_dict:
        a_dict[num] = 1
    else:
        a_dict[num] += 1
    if num == 0:
        ans += 1
    AA.append(num)


def comb(n):
    return n * (n - 1) // 2


for k, v in list(a_dict.items()):
    if v >= 2:
        ans += comb(v)
print(ans)
