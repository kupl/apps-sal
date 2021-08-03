import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))

odd = np.count_nonzero(A % 2 != 0)
four = np.count_nonzero(A % 4 == 0)
ans = 'No'

if odd == 1 and four >= 1:
    ans = 'Yes'
elif odd == 2 and four >= 2:
    ans = 'Yes'
else:
    if odd + four == N and odd - 1 <= four:
        ans = 'Yes'
    elif odd <= four:
        ans = 'Yes'
print(ans)
