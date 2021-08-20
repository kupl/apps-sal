"""
問題：
    高橋君は九九を覚えたので、1 以上 9 以下の 2 つの整数の積を計算することができます。

    整数 N が与えられるので、N を 1 以上 9 以下の 2 つの整数の積として表すことができるか判定し、
    できるなら Yes を、できないなら No を出力して下さい。
"""
'\n制約：\n    1 ≦ N ≦ 100\n    Nは整数である\n'


def abc144b(n: int) -> str:
    for i in range(1, 9 + 1):
        if n % i == 0 and 0 < n // i < 10:
            return 'Yes'
    return 'No'


n = int(input())
print(abc144b(n))
