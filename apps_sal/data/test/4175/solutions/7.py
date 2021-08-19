n = int(input())
w_list = [input()]
ans = 'Yes'
for i in range(n - 1):
    w = input()
    if w not in w_list and w_list[-1][-1] == w[0]:
        w_list.append(w)
    else:
        ans = 'No'
        break
print(ans)
