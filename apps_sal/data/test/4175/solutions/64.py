n = int(input())
words = []
for _ in range(n):
    words.append(input())
sets = set(words)
if len(sets) != len(words):
    ans = 'No'
else:
    for i in range(1, n, 1):
        if words[i - 1][-1] != words[i][0]:
            ans = 'No'
            break
        else:
            ans = 'Yes'
print(ans)
