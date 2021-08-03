n = int(input())
wlist = list(map(int, input().split()))
ans_list = []
for i in range(n - 1):
    ans_list.append(abs(sum(wlist[:i + 1]) - sum(wlist[i + 1:])))
print(min(ans_list))
