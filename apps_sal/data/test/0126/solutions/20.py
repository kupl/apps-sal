3

n = int(input())

str = input()

L = [1, 4, 7]
R = [3, 6, 9]
T = [1, 2, 3]
B = [7, 9]

bl = False
br = False
bt = False
bb = False
b0 = False

for s in str:
    symb = int(s)
    bl = bl or (symb in L)
    br = br or (symb in R)
    bt = bt or (symb in T)
    bb = bb or (symb in B)
    b0 = b0 or (symb == 0)

if (bl and br and bt and bb) or (bt and b0):
    print("YES")
else:
    print("NO")
