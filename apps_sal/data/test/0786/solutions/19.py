n = int(input())
c, d = list(map(int, input().split()))
min_ = 0
max_ = 0
flag = True
if d == 1:
    min_ = 1900
    max_ = float("+Inf")
else:
    min_ = float("-Inf")
    max_ = 1899
for i in range(n - 1):
    c1, d = list(map(int, input().split()))
    if d == 1:
        min_ = max(min_ + c, 1900)
        max_ += c
    else:
        max_ = min(max_ + c, 1899)
        min_ += c
    if min_ > max_:
        flag = False
    c = c1
min_ += c
max_ += c
if not(flag):
    print("Impossible")
elif max_ == float("+Inf"):
    print("Infinity")
else:
    print(max_)
