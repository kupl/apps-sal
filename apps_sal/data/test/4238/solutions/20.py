def multiple_of_nine():
    # 入力
    N = int(input())
    # 処理
    if N % 9 == 0:
        return 'Yes'
    else:
        return 'No'


result = multiple_of_nine()
print(result)
