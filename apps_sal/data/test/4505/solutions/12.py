"""
問題：
    a,b,c からなる長さ 3 の文字列 S が与えられます。
    S を abc を並び替えて作ることができるかどうか判定してください。
"""
'\n制約：\n    |S|=3\n    S は a,b,c からなる\n'


def abc093a(input: str) -> str:
    str_list = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    if input not in str_list:
        return 'No'
    else:
        return 'Yes'


s = str(input())
print(abc093a(s))
