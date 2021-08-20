def valid(num):
    x2 = x0 + disx[n] * (num // n) + disx[num % n]
    y2 = y0 + disy[n] * (num // n) + disy[num % n]
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance <= num


def binsearch(L, R):
    ans = -1
    while L <= R:
        mid = (L + R) // 2
        if valid(mid):
            ans = mid
            R = mid - 1
        else:
            L = mid + 1
    return ans


(x0, y0) = list(map(int, input().split()))
(x1, y1) = list(map(int, input().split()))
n = int(input())
s = input()
disx = [0 for i in range(n + 1)]
disy = [0 for i in range(n + 1)]
for i in range(n):
    disx[i + 1] = disx[i]
    disy[i + 1] = disy[i]
    if s[i] == 'L':
        disx[i + 1] -= 1
    elif s[i] == 'R':
        disx[i + 1] += 1
    elif s[i] == 'U':
        disy[i + 1] += 1
    elif s[i] == 'D':
        disy[i + 1] -= 1
print(binsearch(0, 1000000000000000))
