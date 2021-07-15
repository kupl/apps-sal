A, B = list(map(int, input().split()))
S = input()
cnt = 0

for i in S:
    if i == '-':
        cnt += 1

if cnt == 1:
    post = S.split('-')
    if len(post[0]) == A and len(post[1]) == B:
        print('Yes')
        return

print('No')

