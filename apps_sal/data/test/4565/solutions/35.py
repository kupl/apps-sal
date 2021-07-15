
n = int(input())
A =input()
e = A.count('E')
cnt = e

for i in A:
    if i == 'E':
        cnt -= 1
    else:
        cnt += 1
    e = min(e,cnt)

print(e)
