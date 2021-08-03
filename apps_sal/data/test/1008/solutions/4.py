s = input()
n = int(input())
if len(s) % n == 0:
    for i in range(n):
        t = s[len(s) // n * i:len(s) // n * (i + 1)]
        if t != t[::-1]:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")
