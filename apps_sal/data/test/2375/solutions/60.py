x, y = list(map(int, input().split()))
if abs(x - y) <= 1:
    print("Brown")
else:
    print("Alice")
# a:x+y >1 , abs(x-y)>1
# b:x+y >1 , abs(x-y) <=1
# c:x+y <=1, (abs(x-y) <=1  )　--> lose
#
#       c <--- a <---> b
#       a <---> a
