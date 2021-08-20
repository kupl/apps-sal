from collections import Counter
n = int(input())
l = [input() for i in range(n)]
if Counter(l).most_common()[0][1] != 1:
    ans = 'No'
else:
    l_head = [l[i + 1][0] for i in range(n - 1)]
    l_tail = [l[i][-1] for i in range(n - 1)]
    if l_head == l_tail:
        ans = 'Yes'
    else:
        ans = 'No'
print(ans)
