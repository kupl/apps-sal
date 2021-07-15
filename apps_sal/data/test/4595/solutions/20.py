def resolve():
    """「A*Z」という文字列で最長の長さを出力する
    = 一番左のAと一番右のZでできる文字列
    """
    s = input()
    start_index = s.index("A")
    end_index = s.rindex("Z")
    output = end_index - start_index + 1
    print(output)

resolve()
