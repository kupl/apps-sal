w = input()
ans = 'Yes'
for i in w:
    if w.count(i) % 2 != 0:
        ans = 'No'
        break
print(ans)
