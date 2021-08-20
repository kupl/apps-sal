n = int(input())
w_list = []
ans = 'Yes'
for _ in range(n):
    w = input()
    w_list.append(w)
if len(w_list) != len(set(w_list)):
    ans = 'No'
for i in range(n - 1):
    if w_list[i][-1] != w_list[i + 1][0]:
        ans = 'No'
        break
print(ans)
