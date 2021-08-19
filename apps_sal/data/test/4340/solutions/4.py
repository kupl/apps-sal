def mi():
    return map(int, input().split())


n = int(input())
a = list(mi())
for i in a:
    if i % 2:
        print(i, end=' ')
    else:
        print(i - 1, end=' ')
