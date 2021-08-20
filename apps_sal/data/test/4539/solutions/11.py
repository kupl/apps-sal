n = int(input())
s = str(n)
sum = 0
for i in range(len(s)):
    sum += ord(s[i]) - ord('0')
if n % sum == 0:
    print('Yes')
else:
    print('No')
