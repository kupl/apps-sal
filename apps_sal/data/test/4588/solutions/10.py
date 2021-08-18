A, B = list(map(str, input().split()))

lis = ["A", "B", "C", "D", "E", "F"]
if lis.index(A) < lis.index(B):
    print("<")
elif lis.index(A) == lis.index(B):
    print("=")
else:
    print(">")
