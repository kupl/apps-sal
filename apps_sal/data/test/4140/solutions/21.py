S = list(input())
n = len(S)
lens = n // 2
plus = False
if n % 2 != 0:
    plus = True
test1 = '01' * lens
test2 = '10' * lens
if plus:
    test1 += '0'
    test2 += '1'
(test1, test2) = (list(test1), list(test2))
(count1, count2) = (0, 0)
for i in range(n):
    if S[i] != test1[i]:
        count1 += 1
    if S[i] != test2[i]:
        count2 += 1
print(min(count1, count2))
