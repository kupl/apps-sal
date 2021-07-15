s = str(input())
k = int(input())
if s[:k].count('1') == len(s[:k]):
    print(1)
else:
    for i in s:
        if i != '1':
            print(i)
            break
