import math

(n, p) = tuple(map(int, input().split()))

expection = 0
probability = [0]*n
for i in range(n):
    (l, r) = tuple(map(int, input().split()))
    nump = math.floor(r/p) - math.ceil(l/p) + 1
    numa = r - l + 1
    probability[i] = nump/numa

for i in range(n):
    left = i-1
    right = i+1

    if left == -1:
        left = n-1
    if right == n:
        right = 0

    p_middle = probability[i]
    p_left = probability[left]
    p_right = probability[right]

    expection += (p_middle + (1-p_middle)*p_left*p_right)*2000
    expection += ((1-p_middle)*(p_left*(1-p_right)+(1-p_left)*p_right))*1000

print(str(expection))

