a, b = map(int, input().split())
s = {1, 3, 5, 8, 7, 10, 12}
t = {4, 6, 9, 11}
u = {2}
if a in s and b in s:
    print("Yes")
elif a in t and b in t:
    print("Yes")
elif a in u and b in u:
    print("Yes")
else:
    print("No")
