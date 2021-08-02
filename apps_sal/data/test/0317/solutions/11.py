A = [0] * 26
n = int(input())
s = list(input().lower())
for i in s:
    A[ord(i) - ord('a')] += 1
res = 'YES'
for i in A:
    if i == 0:
        res = 'NO'
print(res)
