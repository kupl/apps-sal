N = int(input())
H = list(map(int, input().split()))

is_mono_inc = True
now = min(H)  # 現ステップでこれより大きい必要
for i in range(N):
    if now <= H[i]:
        now = H[i]
    elif now > H[i] and now <= H[i] + 1:
        now = H[i] + 1
    else:
        is_mono_inc = False

if is_mono_inc:
    print('Yes')
else:
    print('No')
