(a, b, c) = map(int, input().split())
a_ = a % 2
b_ = b % 2
c_ = c % 2
if [a_, b_, c_].count(1) == 0:
    max_ = max([a, b, c])
    print(abs((a - max_ + (b - max_) + (c - max_)) // 2))
elif [a_, b_, c_].count(1) == 1:
    list_ = []
    for i in range(len([a_, b_, c_])):
        if [a_, b_, c_][i] == 0:
            list_.append([a, b, c][i] + 1)
        else:
            list_.append([a, b, c][i])
    max_ = max(list_)
    print(abs(list_[0] - max_ + (list_[1] - max_) + (list_[2] - max_)) // 2 + 1)
elif [a_, b_, c_].count(1) == 2:
    list_ = []
    for i in range(len([a_, b_, c_])):
        if [a_, b_, c_][i] == 1:
            list_.append([a, b, c][i] + 1)
        else:
            list_.append([a, b, c][i])
    max_ = max(list_)
    print(abs(list_[0] - max_ + (list_[1] - max_) + (list_[2] - max_)) // 2 + 1)
else:
    max_ = max([a, b, c])
    print(abs((a - max_ + (b - max_) + (c - max_)) // 2))
