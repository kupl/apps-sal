n = int(input())
spisok = list(map(int, input().split()))
if 0 in spisok:
    print(len(set(spisok)) - 1)
else:
    print(len(set(spisok)))
