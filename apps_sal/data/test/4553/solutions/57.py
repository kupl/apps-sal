import re
A, B = list(map(int, input().split()))
S = input()

ans = 'No'
p = '\d{' + str(A) + '}-\d{' + str(B) + '}'
if re.match(p, S):
    ans = 'Yes'
print(ans)

