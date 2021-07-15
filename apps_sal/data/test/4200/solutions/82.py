n, m = map(int, input().split())
in_list = input().split()
vote_list = [int(i) for i in in_list]

ans = 0
for ai in vote_list:
    if ai >= 1/(4*m)*sum(vote_list):
        ans += 1

if ans < m :
    print('No')
else:
    print('Yes')
