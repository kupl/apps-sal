W = input()
exist_list = []
ans = "No"
for w in W:
    if w in exist_list:
        continue

    if W.count(w) % 2 != 0:
        break

    exist_list.append(w)
else:
    ans = "Yes"

print(ans)

