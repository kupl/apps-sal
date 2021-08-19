def resolve():
    from math import ceil
    # 好きな面から開始できるので、6, 5, 6, 5・・・の繰り返しができる。
    # X//11*2 + (X%11)//6 + floor((X%11)%6)・・・？
    X = int(input())
    print((X // 11) * 2 + ceil((X % 11) / 6))


resolve()
