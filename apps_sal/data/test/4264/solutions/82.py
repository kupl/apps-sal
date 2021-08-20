n = int(input())
l = len(str(n))
if l == 6:
    ans = 90909
elif l == 5:
    ans = n - 9090
elif l == 4:
    ans = 909
elif l == 3:
    ans = n - 90
elif l == 2:
    ans = 9
else:
    ans = n
print(ans)
