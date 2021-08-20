w = input()
for i in w:
    count = 0
    for j in w:
        if i == j:
            count += 1
    if count % 2 != 0:
        ans = 'No'
        break
    else:
        ans = 'Yes'
print(ans)
