a, b = map(int, input().split())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s2.sort()
for i in range(a):
    if s1[i] == 0:
        s1[i] = s2.pop()
if s1 == sorted(s1):
    print("No")
else:
    print("Yes")
