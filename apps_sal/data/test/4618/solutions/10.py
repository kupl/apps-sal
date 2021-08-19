s = input()
K = int(input())

S = set([])
for i in range(len(s)):
    for j in range(i + 1, i + 1 + K):
        # print(f'{s[i:j]=}')
        S.add(s[i:j])
# print(f'{S=}')
# print(f'{sorted(S)=}')
ans = sorted(S)[K - 1]
print(ans)
