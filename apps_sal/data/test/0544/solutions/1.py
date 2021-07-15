t = int(input())
for i in range(t):
    n = int(input())
    a = input()
    flag = True
    for j in range(n // 2):
        if abs(ord(a[j]) - ord(a[-1-j])) > 2 or abs(ord(a[j]) - ord(a[-1-j])) == 1:
            print("NO")
            break
    else:
        print("YES")
