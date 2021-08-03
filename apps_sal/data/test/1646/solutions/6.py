def inpmap():
    return list(map(int, input().split()))


n = int(input())
a = input()
if '1' not in a:
    print(0)
else:
    print("1" + "0" * a.count('0'))
