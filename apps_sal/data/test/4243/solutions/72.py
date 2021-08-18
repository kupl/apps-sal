'''
問題：
    高橋君は金色の硬貨が好きです。
    自分が持っている 500円硬貨 1枚につき 1000、
    5円硬貨 1枚につき 5の嬉しさ を得ます。

    高橋君は X 円を持っています。
    これを高橋君の嬉しさが最大になるように両替したとき、高橋君の嬉しさはいくらになりますか？

    (なお、利用できる硬貨は 500 円玉、100 円玉、50 円玉、10 円玉、5円玉、1 円玉の 6 種類とします。)
'''

'''
    Xは整数
    0 ≦ X ≦ 1,000,000,000
'''


class Yorokobi:
    def __init__(self, money, yorokobi):
        self.money = money
        self.yorokobi = yorokobi

    def calc_yorokobi(self, credit):
        return (credit // self.money) * self.yorokobi


input_x = int(input())

yorokobi_500 = Yorokobi(500, 1000)
yorokobi_5 = Yorokobi(5, 5)

result = 0
if input_x >= 500:
    result += yorokobi_500.calc_yorokobi(input_x)
    result += yorokobi_5.calc_yorokobi(input_x % 500)
else:
    result += yorokobi_5.calc_yorokobi(input_x)

print(result)
