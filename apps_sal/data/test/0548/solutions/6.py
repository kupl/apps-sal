n = int(input())
s = [int(i) for i in input().split()]
u = 0
t = 0
for i in s:
    u+=i
    u%=2
    t+=u
if u:
    print("First")
elif not t:
    print("Second")
else:
    print("First")
