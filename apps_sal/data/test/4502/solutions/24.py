# https://atcoder.jp/contests/abc066/tasks/arc077_a
N = int(input())
N_List = list(map(str, input().split()))
if N % 2 == 0:
    ans = ' '.join(reversed(N_List[1::2])) + ' ' + ' '.join(N_List[::2])
else:
    ans = ' '.join(reversed(N_List[::2])) + ' ' + ' '.join(N_List[1::2])

print(ans)
