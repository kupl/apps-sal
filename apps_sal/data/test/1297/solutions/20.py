def __starting_point():
    import re
    string = input()
    result = sum((1 for a in re.compile('[A]+').findall(string) if len(a) % 2 == 0))
    result += sum((1 for a in re.compile('[T]+').findall(string) if len(a) % 2 == 0))
    result += sum((1 for a in re.compile('[G]+').findall(string) if len(a) % 2 == 0))
    result += sum((1 for a in re.compile('[C]+').findall(string) if len(a) % 2 == 0))
    print(result)


__starting_point()
