S = str(input())

list = []
ans = 'yes'
for s in S:
    for past in list:
        if s == past:
            ans = 'no'
            break
    if ans == 'no':
        break
    list.append(s)

print(ans)
