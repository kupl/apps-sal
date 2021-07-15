n = int(input())
a = list(map(int, input().split()))
bai4 = []
bai2 = []
bai_ = []
for ai in a:
    if ai % 4 == 0:
        bai4.append(ai)
    elif ai % 2 == 0:
        bai2.append(ai)
    else:
        bai_.append(ai)

len_bai_ = len(bai_)
len_bai2 = len(bai2)
len_bai4 = len(bai4)


if len_bai_ > len_bai4:
    if len_bai_ == len_bai4 + 1 and n == len_bai_ + len_bai4:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")
