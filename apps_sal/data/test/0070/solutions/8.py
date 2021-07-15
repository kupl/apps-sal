import sys
n,k = list(map(int, input().split()))
num = list(reversed(str(n)))
ans = 0
zeros = 0
if num.count('0') < k:
    print(len(num) -1)
    return
for ch in  num:
    if ch == '0':
        zeros += 1
        if zeros == k:
            break;
        continue
    ans += 1

print(ans)
