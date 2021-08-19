(n, k) = map(int, input().split())
arr = input()
maxi = 0
for i in range(26):
    temp = arr.count(chr(ord('a') + i))
    if temp > maxi:
        maxi = temp
if maxi > k:
    print('NO')
else:
    print('YES')
