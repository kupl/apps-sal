# ABC165
K = int(input())
A, B = map(int, input().split())
# ----------以上入力----------
K_max = int(B / K) * K
if A <= K_max:
    print('OK')
else:
    print('NG')
