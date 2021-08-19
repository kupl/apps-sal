n = int(input())
s = input()
west_back = s.count('W')
east_back = n - west_back
west_front = 0
east_front = 0
ans = 10 ** 6
for i in range(n):
    if s[i] == 'W':
        west_front += 1
        west_back -= 1
        key = west_front + east_back - 1
    else:
        east_front += 1
        east_back -= 1
        key = west_front + east_back
    ans = min(ans, key)
print(ans)
