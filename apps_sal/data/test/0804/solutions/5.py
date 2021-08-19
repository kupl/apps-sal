def sol():
    s = input()
    k = int(input())
    if k > len(s):
        print('impossible')
    else:
        s = set(s)
        print(max(0, k - len(s)))


sol()
