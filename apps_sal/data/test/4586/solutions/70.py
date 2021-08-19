n = int(input())
if n // 10 % 111 == 0 or n % 1000 % 111 == 0:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
