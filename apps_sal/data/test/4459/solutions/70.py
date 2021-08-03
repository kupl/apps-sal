N = int(input())
a = list(map(int, input().split()))

a_dic = {}

for i in range(N):
    if a[i] not in a_dic.keys():
        a_dic[a[i]] = 1
    else:
        a_dic[a[i]] += 1

ans = 0

for i in a_dic.keys():
    if a_dic[i] >= i:
        ans += a_dic[i] - i
    elif a_dic[i] < i:
        ans += a_dic[i]

print(ans)
