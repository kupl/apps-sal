S = input()
ans_list = []
ans = 753
temp = 0
for s in S:
    ans_list.append(s)
for i in range(len(ans_list) - 2):
    temp = int(ans_list[i]) * 100 + int(ans_list[i + 1]) * 10 + int(ans_list[i + 2])
    comp = abs(temp - 753)
    if ans > comp:
        ans = comp
print(ans)
