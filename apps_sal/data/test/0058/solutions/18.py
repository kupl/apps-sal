n = int(input())
a = int(input())
b = int(input())

if n >= 4 * a + 2 * b:
    ans = 1
elif n >= 4 * a + b:
    ans = 2

elif n >= 4 * a and 2 * b <= n:
    ans = 2


elif n >= 3 * a + 2 * b:
    ans = 2
elif n >= 3 * a and n >= a + 2 * b:
    ans = 2

elif n >= 2 * a + b or n >= 2 * a + 2 * b:
    ans = 2

elif n >= 2 * a and (n >= 2 * b or n >= a + b):
    ans = 3

elif n >= a + 2 * b:
    ans = 4

elif n >= a + b:
    ans = 4

elif n >= 2 * b:
    if 3 * a <= n:
        ans = 3
    else:
        ans = 5

else:
    if 4 * a <= n:
        ans = 3
    elif 3 * a <= n:
        ans = 4
    elif 2 * a <= n:
        ans = 4
    else:
        ans = 6

print(ans)
