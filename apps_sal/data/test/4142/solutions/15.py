S = list(input())
odd = ['R', 'U', 'D']
even = ['L', 'U', 'D']
ans = 'Yes'
for (i, s) in enumerate(S):
    if i % 2 == 0 and s not in odd:
        ans = 'No'
        break
    elif i % 2 == 1 and s not in even:
        ans = 'No'
        break
print(ans)
