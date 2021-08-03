s, v1, v2, t1, t2 = map(int, input().split())
a = 2 * t1 + s * v1
b = 2 * t2 + s * v2
if a < b:
    print("First")
elif a == b:
    print("Friendship")
else:
    print("Second")
