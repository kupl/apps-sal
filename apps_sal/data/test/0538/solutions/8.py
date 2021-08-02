n = input()
n = n.strip('0')
a = n[:]
n = n[::-1]

if n == a:
    print("YES")
else:
    print("NO")
