n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s1 = sum(a)
s2 = sum(b)
if s2>s1:
    print("No")
else:
    print('Yes')
