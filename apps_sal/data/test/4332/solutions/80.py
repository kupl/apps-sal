n = int(input())
ans = 0
for i in str(n):
    ans += int(i)
if n % ans == 0:
    print("Yes")
else:
    print("No")
