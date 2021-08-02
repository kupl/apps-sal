t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    k = s.find('8')
    if k != -1 and len(s) - k >= 11:
        print("YES")
    else:
        print("NO")
