# # aアリス　　　ｂボブ
# a, b = map(int, input().split())
# if a == b:
#     print("Draw")
# elif a == 1:
#     print("Alice")
# elif b == 1:
#     print("Bob")
# elif a < b:
#     print("Bob")
# elif b < a:
#     print("Alice")

x, y = map(int, input().split())

L = list(range(2, 14)) + [1]
a = L.index(x)
b = L.index(y)

if a>b:
    print("Alice")
elif b>a:
    print("Bob")
else:
    print("Draw")
