w = input()

w_list = [a for a in w]
w_set = set(w_list)

ans = 'Yes'
for i in w_set:
    if w_list.count(i)%2 != 0:
        ans = 'No'
        break

print(ans)
