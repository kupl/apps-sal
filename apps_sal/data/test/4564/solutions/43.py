S = input()
past = []
ans = 'yes'
for s in S:
    if s not in past:
        past.append(s)
    else:
        ans = 'no'
        break
print(ans)
