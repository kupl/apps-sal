# coding = SJIS

x, y = list(map(str, input().split()))
alp = ["A", "B", "C", "D", "E", "F"]

if alp.index(x) < alp.index(y):
    print("<")
elif alp.index(x) > alp.index(y):
    print(">")
else:
    print("=")

