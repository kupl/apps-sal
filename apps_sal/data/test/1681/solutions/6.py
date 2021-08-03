a = input()
b = input()
ans = 0
for i in range(ord('a'), ord('z') + 1):
    num1 = sum(ord(j) == i for j in a)
    num2 = sum(ord(j) == i for j in b)
    ans += min(num1, num2)
    if num2 > 0 and num1 == 0:
        print(-1)
        break
else:
    print(ans)
