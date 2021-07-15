n = int(input())
s1 = list(input().strip().split())
s2 = list(input().strip().split())
s1.remove('0')
s2.remove('0')
s1 = ''.join(s1)
s2 = ''.join(s2)
s1 = s1+s1
if s2 in s1:
    print("YES")
else:
    print("NO")

