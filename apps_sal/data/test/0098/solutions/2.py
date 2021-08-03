a1, b1 = list(map(int, input().split()))
a2, b2 = list(map(int, input().split()))
a3, b3 = list(map(int, input().split()))

if a1 - a2 - a3 >= 0 and b2 <= b1 and b3 <= b1:
    print("YES")
elif a1 - a2 - b3 >= 0 and b2 <= b1 and a3 <= b1:
    print("YES")
elif a1 - b2 - a3 >= 0 and a2 <= b1 and b3 <= b1:
    print("YES")
elif a1 - b2 - b3 >= 0 and a2 <= b1 and a3 <= b1:
    print("YES")
elif b1 - a2 - a3 >= 0 and b2 <= a1 and b3 <= a1:
    print("YES")
elif b1 - a2 - b3 >= 0 and b2 <= a1 and a3 <= a1:
    print("YES")
elif b1 - b2 - a3 >= 0 and a2 <= a1 and b3 <= a1:
    print("YES")
elif b1 - b2 - b3 >= 0 and a2 <= a1 and a3 <= a1:
    print("YES")
else:
    print("NO")
