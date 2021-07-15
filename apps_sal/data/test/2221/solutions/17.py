a,b = list(map(int,input().split()))
c,d = list(map(int,input().split()))
n = int(input())
s = input()

janax = [0]*n
janay = [0]*n

if s[0] == 'L':
    janax[0] = -1
elif s[0] == 'R':
    janax[0] = 1

if s[0] == 'D':
    janay[0] = -1
elif s[0] == 'U':
    janay[0] = 1

for i in range(1,n):
    janax[i] = janax[i-1]
    janay[i] = janay[i-1]

    if s[i] == 'L':
        janax[i] += -1
    elif s[i] == 'R':
        janax[i] += 1

    if s[i] == 'D':
        janay[i] += -1
    elif s[i] == 'U':
        janay[i] += 1

def aayenge(duri):
    kitni_baar = duri // n
    kitna_bacha = duri % n

    x = a
    y = b

    x += janax[n-1]*kitni_baar
    y += janay[n-1]*kitni_baar

    if kitna_bacha > 0:
        x += janax[kitna_bacha-1]
        y += janay[kitna_bacha-1]

    return (abs(x-c) + abs(y-d)) <= duri


def lagadiya(left , right):
    ans = -1
    while left <= right:
        mid = (left+right)//2
        if aayenge(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

print(lagadiya(0,10**18))


