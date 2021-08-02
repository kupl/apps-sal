n, k = list(map(int, input().split()))


def good(n, k):
    l = [0] * (k + 1)
    while(n > 0):
        num = n % 10
        n = n // 10
        if(num <= k):
            l[num] += 1
    for i in l:
        if(i == 0):
            return False
    return True


c = 0
for i in range(n):
    num = int(input())
    if(good(num, k)):
        c = c + 1
print(c)
