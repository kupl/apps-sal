n = int(input())
x = list(map(int, input().split()))
ave = sum(x) // len(x)
ans_list = []
ans_list2 = []
for i in x:
    ans = (i - ave) ** 2
    ans_list.append(ans)
ans1 = sum(ans_list)
ave2 = ave + 1
for i in x:
    ans = (i - ave2) ** 2
    ans_list2.append(ans)
ans2 = sum(ans_list2)
if ans1 < ans2:
    print(ans1)
else:
    print(ans2)
