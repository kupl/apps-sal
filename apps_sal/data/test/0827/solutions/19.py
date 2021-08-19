from collections import Counter
N = int(input())
S = input()
n = Counter(S)['0']
if S in '110' * (n * 3 + 3):
    if S == '1':
        print(2 * 10 ** 10)
    else:
        ans = 10 ** 10 - n
        if S[-1] == '0':
            ans += 1
        print(ans)
else:
    print(0)
