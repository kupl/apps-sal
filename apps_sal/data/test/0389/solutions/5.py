import sys
#sys.stdin = open('prefrev.in', 'r')
#sys.stdout = open('prefrev.out', 'w')
n, m = map(int, input().split())
divs = [2, 3, 5]
ar = [0] * 6
br = [0] * 6
tn = n; tm = m
for i in divs:
    while tn % i == 0 and tn > 0:
        ar[i] += 1
        tn //= i
    while tm % i == 0 and tm > 0:
        br[i] += 1
        tm //= i
print
if tn != tm:
    print('-1')
else:
    # print('ok')
    ans = 2e9
    for i in range(min(br[2], ar[2]) + 1):
        for j in range(min(br[3], ar[3]) + 1):
            for k in range(min(br[5], ar[5]) + 1):
                if ar[2] - i + br[2] - i + ar[3] - j + br[3] - j + ar[5] - k + br[5] - k < ans:
                    ans = ar[2] - i + br[2] - i + ar[3] - j + br[3] - j + ar[5] - k + br[5] - k
    print(ans)
