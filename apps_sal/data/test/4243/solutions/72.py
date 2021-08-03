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

    def calc_yorokobi(self, credit):    # credit （残金？）を入力として受け取り、喜びを計算して返す
        return (credit // self.money) * self.yorokobi


# 標準入力から X の値を取得する
input_x = int(input())

yorokobi_500 = Yorokobi(500, 1000)
yorokobi_5 = Yorokobi(5, 5)

result = 0  # 結果格納用
if input_x >= 500:
    result += yorokobi_500.calc_yorokobi(input_x)   # 高橋君 500円の喜び
    result += yorokobi_5.calc_yorokobi(input_x % 500)   # 高橋君 5円の喜び
else:
    result += yorokobi_5.calc_yorokobi(input_x)

print(result)

# ret1 = input_x // 500  # 500円で割った商
# ret2 = ret1 * 1000  # 高橋君 500円の喜び
# ret3 = input_x - (ret1 * 500)   # X円から500円の枚数分を引いたお金
# ret4 = ret3 // 5 # （X円から500円の枚数分を引いたお金）÷ 5
# ret5 = ret4 * 5 # 高橋君 5円の喜び
# print(ret2 + ret5)
